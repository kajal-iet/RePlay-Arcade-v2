from langchain_community.llms import Ollama

def get_llm():
    return Ollama(
        model="llama3",
        temperature=0.2,
        num_ctx=4096
    )
