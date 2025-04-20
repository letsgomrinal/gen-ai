# gen-ai


# `ollama` command:

- download 
```
brew install ollama
```

```
ollama run llama3.2
```

- available models:

```
ollama run llama2
ollama run codellama
ollama run gemma
ollama run phi
```

- serve model
```
ollama serve
```

- make api request:

```
curl http://localhost:11434/api/generate -d '{
  "model": "llama3.2",
  "prompt": "Explain relativity in simple terms"
}'
```
- embedding model
```
ollama pull nomic-embed-text
```

# Install `uv` package manager

- Installing `uv`:

```
curl -Ls https://astral.sh/uv/install.sh | sh
```