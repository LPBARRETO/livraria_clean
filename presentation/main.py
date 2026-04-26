from fastapi import FastAPI
from fastapi.responses import RedirectResponse  # <-- Adicione esta linha
from core.use_cases import LivrariaUseCases
from infrastructure.txt_repository import TXTLivroRepository

app = FastAPI()

repositorio_txt = TXTLivroRepository()
casos_de_uso = LivrariaUseCases(repositorio_txt)

# --- Adicione este bloco ---
@app.get("/", include_in_schema=False)
async def rota_raiz():
    # Redireciona o professor direto para a tela de testes!
    return RedirectResponse(url="/docs")
# ---------------------------

@app.get("/catalogo")
async def ver_catalogo():
    return casos_de_uso.obter_catalogo()

@app.post("/checkout/{id_livro}")
async def comprar(id_livro: int):
    sucesso, mensagem = casos_de_uso.realizar_checkout(id_livro)
    return {"status": sucesso, "mensagem": mensagem}

@app.post("/repor/{id_livro}")
async def repor(id_livro: int):
    sucesso, mensagem = casos_de_uso.repor_estoque(id_livro)
    return {"status": sucesso, "mensagem": mensagem}
