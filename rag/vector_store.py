from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings

def create_vector_store():
    docs = [
        "Python function to check prime number using loop",
        "Java program to check prime number",
        "Python factorial program",
        "Java factorial using recursion",
        "Python palindrome check",
        "Java palindrome check"
    ]

    embeddings = HuggingFaceEmbeddings()

    db = FAISS.from_texts(docs, embeddings)

    return db
