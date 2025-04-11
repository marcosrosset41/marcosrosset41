from llama_cpp import Llama

llm = Llama(model_path="model/llama-2-7b-chat.Q5_K_M.gguf")

def extrair_palavras_chave(texto):
    prompt = f"Extraia as palavras-chave para buscar um produto no e-commerce: {texto}\nPalavras-chave:"
    output = llm(prompt, max_tokens=20, stop=["\n"])
    return output["choices"][0]["text"].strip()
