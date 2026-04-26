from .interfaces import LivroRepositoryInterface

class LivrariaUseCases:
    # A Inversão de Dependência na prática: injetamos a interface, não o TXT!
    def __init__(self, repository: LivroRepositoryInterface):
        self.repo = repository

    def obter_catalogo(self):
        return self.repo.listar_todos()

    def realizar_checkout(self, id_livro: int):
        livro = self.repo.buscar_por_id(id_livro)
        if livro and livro.estoque > 0:
            livro.estoque -= 1
            self.repo.salvar(livro) # Manda salvar a alteração
            return True, "Compra PIX aprovada!"
        return False, "Erro: Livro indisponível no estoque."

    # --- A NOVA FEATURE ---
    def repor_estoque(self, id_livro: int):
        livro = self.repo.buscar_por_id(id_livro)
        if livro:
            livro.estoque += 1
            self.repo.salvar(livro)
            return True, f"Estoque do livro '{livro.titulo}' reposto com sucesso!"
        return False, "Livro não encontrado."