from fastapi import FastAPI, Request
from llm_llama import extrair_palavras_chave
from scraper import buscar_melhor_preco
from fastapi.responses import JSONResponse

app = FastAPI()

@app.get("/")
def root():
    return {"status": "online"}

@app.post("/mensagem")
async def receber_mensagem(request: Request):
    dados = await request.json()
    mensagem = dados.get("mensagem")

    if not mensagem:
        return {"erro": "Mensagem vazia"}

    try:
        palavras_chave = extrair_palavras_chave(mensagem)
        resultado = buscar_melhor_preco(palavras_chave)
        return {"resposta": resultado}
    except Exception as e:
        return JSONResponse(status_code=500, content={"erro": str(e)})
