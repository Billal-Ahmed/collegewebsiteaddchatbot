
import faiss 
import numpy as np 
import torch
from transformers import AutoTokenizer, AutoModel




# Load a transformer model for embeddings
model_name = 'sentence-transformers/all-MiniLM-L6-v2'

# Try loading the tokenizer and model with a fallback for errors
try:
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModel.from_pretrained(model_name)
except Exception as e:
    print(f"Error loading model: {e}")
    raise

# Convert the documents into embeddings
def embed_documents(documents):
    inputs = tokenizer(documents, return_tensors='pt', padding=True, truncation=True)
    with torch.no_grad():
        embeddings = model(**inputs).last_hidden_state.mean(dim=1)
    return embeddings


#chn
def build_faiss_index(embeddings):
    # Determine the dimension of embeddings (e.g., 768 for BERT)
    dimension = embeddings.shape[1]

    # Create FAISS index using L2 distance (Euclidean distance)
    index = faiss.IndexFlatL2(dimension)
    
    # Add embeddings to the FAISS index
    index.add(embeddings)
    
    return index



# Build FAISS index
# def build_faiss_index(doc_embeddings):
#     index = faiss.IndexFlatL2(doc_embeddings.shape[1])  # L2 distance
#     index.add(doc_embeddings)
#     return index




# Search FAISS index for similar documents
def search_faiss_index(index, query, k=2):
    query_embedding = embed_documents([query]).cpu().numpy()
    #masla
    D, I = index.search(query_embedding, k)
    return I
