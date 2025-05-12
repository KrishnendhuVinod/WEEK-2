#Import libraries
import chromadb
import numpy as np  

# Initialize ChromaDB Client
client = chromadb.Client()

# Create a collection
collection = client.create_collection(name="my_collection")

# Sample documents to be added to the collection
documents = [
    "ChromaDB is a powerful vector database that helps in storing and searching documents using embeddings.",
    "ChromaDB allows efficient similarity search and retrieval of documents by converting them into vector embeddings."
]

# Use basic dummy embeddings
dummy_embeddings = np.random.random((len(documents), 512)).tolist()  

# Add documents to the ChromaDB collection
collection.add(
    documents=documents,
    metadatas=[{"source": "document1"}, {"source": "document2"}],  
    ids=["id1", "id2"],  
    embeddings=dummy_embeddings  
)

print("Sample documents stored in ChromaDB with dummy embeddings.")
# Query all documents in the collection
results = collection.get(include=["documents", "metadatas", "embeddings"])

# Display the retrieved documents and their metadata
print("\nRetrieved Documents from ChromaDB:")
for doc, meta in zip(results["documents"], results["metadatas"]):
    print(f"Document: {doc}")
    print(f"Metadata: {meta}\n")