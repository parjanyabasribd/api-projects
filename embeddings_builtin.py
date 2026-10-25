import chromadb
from dotenv import load_dotenv
from chromadb.utils.embedding_functions import GoogleGeminiEmbeddingFunction

load_dotenv()

docs = [
    "Filter coffee is traditionally served in a steel tumbler and davara.",
    "Monsoon clouds gather over the Western Ghats in June.",
    "A cricket match can be decided in the very last over.",
    "Sourdough bread needs a live starter and a long, slow fermentation.",
    "Tomato plants need at least six hours of direct sunlight every day.",
    "A leaky tap can waste hundreds of litres of water in a month.",
    "The Sicilian Defense leads to sharp, unbalanced games of chess.",
    "Old paperback books develop a distinct smell as the paper ages.",
]

chroma_client = chromadb.PersistentClient(path="./chroma_db_builtin")
collection = chroma_client.get_or_create_collection(
    name="everyday_docs", 
    embedding_function=GoogleGeminiEmbeddingFunction(
        model_name="gemini-embedding-001")
)

collection.upsert(ids=[f"doc_{i}" for i in range(len(docs))], documents=docs)
print("Docs in collection:", collection.count())

queries = [
    "What do I need to bake a loaf using natural yeast?",
    "Why is my water bill so high?",
    "Which morning drink is popular in Karnataka?",
    "When does the rainy season begin?",
    "How do rockets reach orbit?",
]

results = collection.query(query_texts=queries, n_results=1)

for i, q in enumerate(queries):
    print(f"\nQuery: {q}")
    for doc, dist in zip(results["documents"][i], results["distances"][i]):
        print(f"  {dist:.3f}  {doc}")