from src.infra.repository import AtoresRepo, FilmesRepo
from src.infra.configs.connection import DBConnectionHandler

repo = AtoresRepo()
data = repo.select()
print(data)

repo2 = FilmesRepo(DBConnectionHandler)
data2 = repo2.select()
print(data2[0].atores)

# from src.infra.repository.filmes import FilmesRepo
#
# repo = FilmesRepo()
# repo.insert("Vingadores", "acao", 2012)
# repo.delete("Vingadores")
# data = repo.select()
# print(data)
