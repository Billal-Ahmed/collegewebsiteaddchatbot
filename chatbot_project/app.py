from flask import Flask, jsonify, render_template, request
from embeddings import embed_documents, build_faiss_index, search_faiss_index
from text_generation import groq_generate

app = Flask(__name__)

# Load documents
with open('data/documents.txt', 'r') as f:
    documents = f.read().splitlines()

# Embed documents and build FAISS index
doc_embeddings = embed_documents(documents).cpu().numpy()
index = build_faiss_index(doc_embeddings)

# Set your Groq API key
api_key = '****************************8'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_response', methods=['POST'])
def get_response():
    query = request.json['query']  # Get the prompt from the JSON request

    # Print query for debugging
    print("User Query:", query)

    # Embed the user query
    query_embedding = embed_documents([query]).cpu().numpy()  # Make sure to embed the query

    # Search for relevant documents
    top_docs_indices = search_faiss_index(index, query_embedding)  # Use the embedded query
    print("Top Document Indices:", top_docs_indices)  # Print the indices of the top documents

    retrieved_docs = [documents[i] for i in top_docs_indices[0]]

    # Combine retrieved docs into one prompt for text generation
    combined_prompt = " ".join(retrieved_docs) + " " + query

    # Generate response using Groq API
    generated_response = groq_generate(combined_prompt, api_key)

    # Print the generated response to the console
    print("Generated Response:", generated_response)

    return jsonify({'response': generated_response})  # Return response as JSON

if __name__ == '__main__':
    app.run(debug=True)
