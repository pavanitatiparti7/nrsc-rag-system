import chromadb

client = chromadb.PersistentClient(path="chroma_db")

collection = client.get_or_create_collection(
    name="nrsc_documents"
)

def store_chunks(chunks, embeddings):

    for i, (chunk, embedding) in enumerate(zip(chunks, embeddings)):

        collection.add(
            documents=[chunk],
            embeddings=[embedding.tolist()],
            ids=[str(i)]
        )