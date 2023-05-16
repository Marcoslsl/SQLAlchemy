from src.infra.repository.filmes import FilmesRepo

repo = FilmesRepo()
repo.insert("Vingadores", "acao", 2012)
repo.delete("Vingadores")
data = repo.select()
print(data)
