from langchain_community.llms import Ollama

llm = Ollama(model="llama3.2")
response = llm.invoke("What's the modern Gen AI stack?")
print(response)