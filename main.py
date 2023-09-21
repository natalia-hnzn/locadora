from infra.repository.filme_repository import FilmeRepository
from infra.configs.connection import DBConnectionHandler

repo = FilmeRepository()
data_base = DBConnectionHandler()
repo.insert('Barbie', 'Comédia', 2023)
repo.insert('Spawn', 'Ação', 1997)

filmes = repo.select_all()
print('filmes')

repo.update(2, 'Spawn - Soldado do inferno', 'Ação', 1997)
filme = repo.select_one(2)

print(filme)

id = len('filmes')
repo.delete(id)
