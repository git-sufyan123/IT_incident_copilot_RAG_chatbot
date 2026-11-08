import pandas as pd


def chunk_ticket(ticket: dict) -> dict:
    ticket_id = ticket["ticket_id"]

    fields = {
        "Incident": ticket["incident_title"],
        "Description": ticket["incident_description"],
        "Investigation": ticket["investigation_notes"],
        "Root Cause": ticket["root_cause"],
        "Historical Resolution": ticket["resolution_summary"],
        "Resolution Steps": ticket["resolution_steps"],
        "Verification": ticket["verification"],
    }

    text = "\n\n".join(
        f"{label}: {value}"
        for label, value in fields.items()
        if pd.notna(value)
    )

    return {
        "chunk_id": ticket_id,
        "parent_id": ticket_id,
        "source_type": "ticket",
        "synthetic": True,
        "category": ticket["category"],
        "subcategory": ticket["subcategory"],
        "priority": ticket["priority"],
        "related_runbook": ticket["related_runbook"],
        "created_at": ticket["created_at"],
        "text": text,
    }


if __name__ == "__main__":
    df = pd.read_csv("data/raw/resolved_it_incidents_1000.csv")
    chunks = [chunk_ticket(row) for row in df.to_dict("records")]

    print("Total tickets:", len(df))
    print("Total chunks:", len(chunks))
    print("\nFirst chunk:\n")
    print(chunks[0])