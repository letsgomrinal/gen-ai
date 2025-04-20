import requests
import json

def get_ollama_embedding(prompt: str, model: str = "nomic-embed-text"):
    url = "http://localhost:11434/api/embeddings"
    payload = {
        "model": model,
        "prompt": prompt
    }

    response = requests.post(url, json=payload)
    response.raise_for_status()

    embedding = response.json()["embedding"]
    return embedding

# Example usage
if __name__ == "__main__":
    text = "Ollama makes it easy to run LLMs locally."
    embedding = get_ollama_embedding(text)
    print(f"Embedding length: {len(embedding)}")
    print(f"First 5 values: {embedding[:5]}")
