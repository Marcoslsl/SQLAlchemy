from src.infra.configs.connection import DBConnectionHandler
from src.infra.entities import Atores, Filmes


class AtoresRepo:
    def select(self):
        with DBConnectionHandler() as db:
            data = (
                db.session.query(Atores)
                .join(Filmes, Atores.titulo_filme == Filmes.titulo)
                .with_entities(Atores.nome, Filmes.genero, Filmes.titulo)
                .all()
            )
            return data
