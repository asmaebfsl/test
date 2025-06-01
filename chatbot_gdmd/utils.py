import json

def load_all_metadata():
    files = ["emdat_metadata.json", "desinventar_metadata.json", "gdmd_metadata.json"]
    datasets = []
    for file in files:
        with open(file, "r") as f:
            datasets.append(json.load(f))
    return datasets

def search_all_metadata(query):
    query = query.lower()
    results = []
    for data in load_all_metadata():
        if any(kw in query for kw in data.get("keywords", [])):
            results.append(data)
        elif query in data.get("description", "").lower():
            results.append(data)
    return results