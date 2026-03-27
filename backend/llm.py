import os
import requests
from dotenv import load_dotenv
# Use environment variable (SAFE)
load_dotenv()
API_KEY = os.getenv("GROQ_API_KEY")

def generate_response(prompt):
    url = "https://api.groq.com/openai/v1/chat/completions"

    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

    data = {
        "model": "llama-3.1-8b-instant",
        "messages": [
           {"role": "system", "content": "You are an expert full-stack developer. Always generate complete project code including frontend and backend files. Return structured code for each file."},
            {"role": "user", "content": prompt}
        ]
    }

    response = requests.post(url, headers=headers, json=data)

    
    if response.status_code != 200:
        return f"Error: {response.text}"

    return response.json()["choices"][0]["message"]["content"]