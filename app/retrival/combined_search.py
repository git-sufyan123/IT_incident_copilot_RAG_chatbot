from app.retrival.search_runbooks import (
    embed_query,
    qdrant,
)

RUNBOOK_COLLECTION = "it_incident_runbooks"
TICKET_COLLECTION = "it_incident_tickets"


def retrieve(query: str, runbook_limit=3, ticket_limit=5):
    vector = embed_query(query)

    # Retrieve more child chunks than the number of
    # unique runbooks we want.
    runbook_results = qdrant.query_points(
        collection_name=RUNBOOK_COLLECTION,
        query=vector,
        limit=15,
        with_payload=True,
    ).points

    ticket_results = qdrant.query_points(
        collection_name=TICKET_COLLECTION,
        query=vector,
        limit=ticket_limit,
        with_payload=True,
    ).points

    # Deduplicate runbook results by parent ID.
    unique_runbooks = {}

    for point in runbook_results:
        parent_id = point.payload["parent_id"]

        if parent_id not in unique_runbooks:
            unique_runbooks[parent_id] = {
                "runbook_id": parent_id,
                "score": point.score,
                "section": point.payload["section"],
                "status": point.payload["status"],
                "text": point.payload["text"],
            }

        if len(unique_runbooks) >= runbook_limit:
            break

    tickets = []

    for point in ticket_results:
        tickets.append({
            "ticket_id": point.payload["parent_id"],
            "score": point.score,
            "related_runbook": point.payload["related_runbook"],
            "text": point.payload["text"],
        })

    return {
        "runbooks": list(unique_runbooks.values()),
        "tickets": tickets,
    }


if __name__ == "__main__":
    try:
        query = input("Describe an IT incident: ").strip()
        results = retrieve(query)

        print("\n=== RELEVANT RUNBOOKS ===")
        for runbook in results["runbooks"]:
            print(
                f"{runbook['runbook_id']} | "
                f"Score: {runbook['score']:.4f} | "
                f"Section: {runbook['section']}"
            )

        print("\n=== SIMILAR HISTORICAL TICKETS ===")
        for ticket in results["tickets"]:
            print(
                f"{ticket['ticket_id']} | "
                f"Score: {ticket['score']:.4f} | "
                f"Related: {ticket['related_runbook']}"
            )
    finally:
        from app.retrival.search_runbooks import gemini
        gemini.close()
        qdrant.close()