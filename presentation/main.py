from fastapi import FastAPI
from core.use_cases import LivrariaUseCases
from infrastructure.txt_repository import TXTLivroRepository

app = FastAPI()

# Montando os blocos (Injeção de Dependência)
# O FastAPI conhece o TXT, mas passa ele escondido para o Caso de Uso
repositorio_txt = TXTLivroRepository()
casos_de_uso = LivrariaUseCases(repositorio_txt)

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
