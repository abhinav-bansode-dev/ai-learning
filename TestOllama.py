from langchain_ollama import OllamaLLM

llm = OllamaLLM(model="mistral")  # or another model you’ve pulled
response = llm.invoke("What is AI?")
print(response)


'''🔹What You’ve Achieved
✅ Installed langchain-ollama (correct package).

✅ Connected Ollama with LangChain.

✅ Verified output using mistral.'''