from load_runbooks import load_runbooks


def format_section(title, items):
    return f"{title}:\n" + "\n".join(
        f"- {item}" for item in items
    )


def chunk_runbook(runbook):
    runbook_id = runbook["id"]
    title = runbook["title"]

    sections = {
        "context": [
            f"Title: {title}",
            f"Purpose: {runbook['purpose']}",
            format_section("Symptoms", runbook["symptoms"]),
            format_section("Prerequisites", runbook["prerequisites"]),
        ],
        "procedure": [
            f"Title: {title}",
            format_section("Prerequisites", runbook["prerequisites"]),
            format_section("Steps", runbook["steps"]),
            format_section("Cautions", runbook["cautions"]),
        ],
        "recovery": [
            f"Title: {title}",
            format_section("Verification", runbook["verification"]),
            format_section("Rollback", runbook["rollback_recovery"]),
            format_section("Escalation", runbook["escalation"]),
            format_section("Cautions", runbook["cautions"]),
        ],
    }

    chunks = []

    for section, content in sections.items():
        chunks.append({
            "chunk_id": f"{runbook_id}-{section}",
            "parent_id": runbook_id,
            "source_type": "runbook",
            "section": section,
            "category": runbook["category"],
            "version": runbook["version"],
            "status": runbook["status"],
            "synthetic": runbook["synthetic"],
            "text": "\n\n".join(content),
        })

    return chunks


if __name__ == "__main__":
    runbooks = load_runbooks("data/runbooks.jsonl")

    all_chunks = []

    for runbook in runbooks:
        all_chunks.extend(chunk_runbook(runbook))

    print("Total runbooks:", len(runbooks))
    print("Total chunks:", len(all_chunks))
    print("\nExample chunk:\n")
    print(all_chunks[0])
