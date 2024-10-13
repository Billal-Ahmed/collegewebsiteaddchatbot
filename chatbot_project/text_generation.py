import os
from groq import Groq

# Groq API client setup
client = Groq(api_key=os.environ.get("GROQ_API_KEY"))  # Make sure to set your API key in the environment

def groq_generate(prompt):
    # Call the Groq API to generate text
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": prompt,
            }
        ],
        model="llama3-8b-8192",  # Use the correct model, adjust this if needed
    )
    
    # Return the generated response
    return chat_completion.choices[0].message.content