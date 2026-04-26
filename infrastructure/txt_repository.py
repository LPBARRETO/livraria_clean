import os
from core.interfaces import LivroRepositoryInterface
from core.entities import Livro

class TXTLivroRepository(LivroRepositoryInterface):
    def __init__(self, file_path="estoque.txt"):
        self.file_path = file_path
        self._inicializar_arquivo()

    def _inicializar_arquivo(self):
        # Se o arquivo não existe, cria um com dados iniciais
        if not os.path.exists(self.file_path):
            with open(self.file_path, "w", encoding="utf-8") as f:
                f.write("1,Engenharia de Software,85.00,5\n")
                f.write("2,Código Limpo,70.00,3\n")
                f.write("3,Física 3 e Instalações,120.00,1\n")

    def listar_todos(self):
        livros = []
        with open(self.file_path, "r", encoding="utf-8") as f:
            for linha in f:
                dados = linha.strip().split(",")
                if len(dados) == 4:
                    livros.append(Livro(int(dados[0]), dados[1], float(dados[2]), int(dados[3])))
        return livros

    def buscar_por_id(self, id_livro: int):
        for l in self.listar_todos():
            if l.id == id_livro:
                return l
        return None

    def salvar(self, livro: Livro):
        livros = self.listar_todos()
        with open(self.file_path, "w", encoding="utf-8") as f:
            for l in livros:
                # Atualiza a linha se for o livro alterado, ou mantém igual
                if l.id == livro.id:
                    f.write(f"{livro.id},{livro.titulo},{livro.preco},{livro.estoque}\n")
                else:
                    f.write(f"{l.id},{l.titulo},{l.preco},{l.estoque}\n")