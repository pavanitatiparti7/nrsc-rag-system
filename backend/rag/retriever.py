import chromadb
from sentence_transformers import SentenceTransformer

client = chromadb.PersistentClient(path="chroma_db")

collection = client.get_or_create_collection(
    name="nrsc_documents"
)

model = SentenceTransformer('all-MiniLM-L6-v2')

def retrieve_relevant_chunks(query, top_k=3):

    query_embedding = model.encode(query).tolist()

    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=top_k
    )

    documents = results['documents'][0]

    return documents