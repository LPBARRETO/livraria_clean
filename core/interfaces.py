from abc import ABC, abstractmethod
from typing import List
from .entities import Livro

class LivroRepositoryInterface(ABC):
    @abstractmethod
    def listar_todos(self) -> List[Livro]: pass

    @abstractmethod
    def buscar_por_id(self, id_livro: int) -> Livro: pass

    @abstractmethod
    def salvar(self, livro: Livro): pass