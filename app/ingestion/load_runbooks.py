import json
from pathlib import Path

def load_runbooks(file_path: str) -> list[dict]:
    runbooks = []
    seen_ids = set()

    with open(file_path, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line:
                runbook = json.loads(line)
                if runbook["id"] in seen_ids:
                    raise ValueError(f"Duplicate runbook ID found: {runbook['id']}")
                seen_ids.add(runbook["id"])
                runbooks.append(runbook)
                

    return runbooks

if __name__ == "__main__":
    path = "data/raw/runbooks.jsonl"

    records = load_runbooks(path)

    print("Total runbooks:", len(records))
    print("First runbook ID:", records[0]["id"])
    print("First runbook title:", records[0]["title"])
