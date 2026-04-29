memory_db = []

def store_memory(error, fix):
    memory_db.append({
        "error": error,
        "fix": fix
    })


def retrieve_memory(query):
    results = []

    for item in memory_db:
        if query.lower() in item["error"].lower():
            results.append(item["fix"])

    return "\n".join(results[:2])
