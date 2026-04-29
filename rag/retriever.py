from rag.vector_store import create_vector_store

db = create_vector_store()

def retrieve_context(query):
    results = db.similarity_search(query, k=2)
    return "\n".join([r.page_content for r in results])
