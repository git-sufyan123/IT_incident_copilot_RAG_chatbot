# IT Incident Copilot Synthetic Dataset

1,000 synthetic RESOLVED IT incidents for an evidence-grounded RAG/IT Incident Resolution Copilot.

All content is artificial and contains no real employee, customer, company, credential, or incident information.

## Recommended file
Use `resolved_it_incidents_1000.jsonl` for RAG ingestion.

## Important fields
`incident_title`, `incident_description`, `investigation_notes`, `root_cause`, `resolution_summary`, `resolution_steps`, `verification`, `related_kb`, `related_runbook`.

Keep `ticket_id`, category, subcategory, priority, assignment_group and dates as vector-store metadata.

## Suggested RAG document
TITLE + CATEGORY + SYMPTOMS + INVESTIGATION + ROOT CAUSE + RESOLUTION + VERIFICATION + SOURCE IDs.

The dataset intentionally contains repeated incident patterns with different metadata so retrieval can learn that similar symptoms can have different causes.
