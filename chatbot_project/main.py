from embeddings import embed_documents, build_faiss_index, search_faiss_index
from text_generation import groq_generate






# Load documents
with open('data/documents.txt', 'r') as f:
    documents = f.read().splitlines()



# Embed documents and build FAISS index
doc_embeddings = embed_documents(documents).cpu().numpy()
index = build_faiss_index(doc_embeddings)




def chatbot(query):
    # Search for relevant documents
    top_docs_indices = search_faiss_index(index, query)
    
    retrieved_docs = [documents[i] for i in top_docs_indices[0]]

    # Combine retrieved docs into one prompt for text generation
    combined_prompt = " ".join(retrieved_docs) + " " + query

    # Generate response using Groq API
    generated_response = groq_generate(combined_prompt)
    return generated_response

# Example query
query = "tell me about degree college skardu"
response = chatbot(query)
print("Chatbot Response:", response)


