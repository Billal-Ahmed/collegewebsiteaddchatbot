

# College Website Chatbot with Groq API and FAISS Document Retrieval

This project implements a chatbot integrated with a cloned version of a college website. The chatbot is designed to provide relevant, AI-generated responses based on user queries. By leveraging FAISS indexing for document retrieval and the Groq API for language processing, this chatbot delivers efficient and contextually appropriate responses.

## Table of Contents

1. [Project Overview](#project-overview)
2. [Technologies Used](#technologies-used)
3. [Setup Instructions](#setup-instructions)
4. [Directory Structure](#directory-structure)
5. [Features](#features)
6. [Enhanced Document Retrieval and Contextual Response Generation](#enhanced-document-retrieval-and-contextual-response-generation)
7. [API Routes](#api-routes)
8. [Usage](#usage)
9. [Future Improvements](#future-improvements)
10. [Contributing](#contributing)
11. [License](#license)

## Project Overview

This project is a Flask-based web application that serves as an interactive chatbot for a college website. The cloned college website is fully functional and styled using HTML, CSS, and JavaScript. The chatbot uses the Groq API and the FAISS library for embedding, indexing, and retrieving documents based on user input. The Groq-powered LLM (LLAMA 3.1 with 8B parameters) is employed to generate accurate and contextually relevant responses by sending specific queries based on the documents retrieved.

## Technologies Used

- **Frontend**: HTML, CSS, JavaScript
- **Backend**: Flask, Python
- **Document Retrieval**: FAISS (Facebook AI Similarity Search)
- **LLM**: Groq API (LLAMA 3.1 with 8B parameters)
- **Additional Libraries**: Groq client library, FAISS library

## Setup Instructions

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/username/college-chatbot.git
   cd college-chatbot
   ```

2. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Set the Groq API Key**:
   - In the code, replace the placeholder API key with your actual Groq API key.

4. **Run the Application**:
   ```bash
   python app.py
   ```

5. **Access the Chatbot**:
   Open your web browser and go to `http://127.0.0.1:5000/`.

## Directory Structure

```
college-chatbot/
├── static/             # Contains CSS, JavaScript, and images
├── templates/          # Contains HTML templates
├── data/
│   └── documents.txt   # The text file with documents for FAISS indexing
├── app.py              # Main application file
├── embeddings.py       # Contains functions for FAISS embeddings
├── text_generation.py  # Contains functions for interacting with the Groq API
└── README.md           # Documentation
```

## Features

- **Chatbot with Custom Prompts**: Users can ask questions on the website, and the chatbot responds with information generated using Groq's LLM.
- **Document Retrieval with FAISS**: This application embeds and indexes documents for efficient retrieval of relevant information.
- **Interactive Frontend**: Chat UI is designed to feel integrated with the website, providing instant updates based on the user query.
- **RESTful API**: Uses Flask to handle HTTP POST requests for interactions with the chatbot.

## Enhanced Document Retrieval and Contextual Response Generation

To improve the contextual relevance of responses, the chatbot employs FAISS indexing. This setup works by embedding each document from the `documents.txt` file and building a FAISS index. The user's query is also embedded and matched against the FAISS index to identify the most relevant documents, which are then sent as part of the prompt to the Groq-powered LLM.

By integrating FAISS with Groq, the system can:

1. **Efficiently Retrieve Contextual Information**: Only the most relevant documents are included in the prompt, resulting in more focused and accurate responses.
2. **Optimize Performance**: Embedding documents ahead of time reduces computation during user queries, making the system faster and more scalable.

## API Routes

### `GET /`

Renders the main HTML page (`index.html`), which serves as the user interface for interacting with the chatbot.

### `POST /get_response`

Receives a JSON object containing a `query` from the client, retrieves relevant documents using FAISS, and sends the combined prompt to Groq's API. The API then generates a response, which is sent back to the client in JSON format.

Sample request payload:
```json
{
    "query": "What can you tell me about the history of the college?"
}
```

Sample response payload:
```json
{
    "response": "The college was established in ..."
}
```

## Usage

1. Open the website in a web browser, and interact with the chatbot by entering a query in the input box.
2. Click on the submit button. The chatbot will retrieve relevant documents, generate a response using Groq's API, and display the response on the page.

## Future Improvements

- **Fine-Tuning the LLM**: Currently, the LLM is not fine-tuned. Fine-tuning with a larger dataset could improve response accuracy.
- **Persistent User Sessions**: Implementing persistent sessions to maintain context over multiple queries.
- **UI Enhancements**: Adding features like typing indicators and response loading animations for a more interactive experience.

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue with your suggestions.

## License
..................
