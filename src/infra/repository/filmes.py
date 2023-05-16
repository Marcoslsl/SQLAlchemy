from src.infra.configs.connection import DBConnectionHandler
from src.infra.entities.filmes import Filme


class FilmesRepo:
    def select(self):
        with DBConnectionHandler() as db:
            data = db.session.query(Filme).all()
            return data

    def insert(self, titulo, genero, ano):
        with DBConnectionHandler() as db:
            data_insert = Filme(titulo=titulo, genero=genero, ano=ano)
            db.session.add(data_insert)
            db.session.commit()

    def delete(self, titulo):
        with DBConnectionHandler() as db:
            db.session.query(Filme).filter(Filme.titulo == titulo).delete()
            db.session.commit()

    def update(self, titulo, ano):
        with DBConnectionHandler() as db:
            db.session.query(Filme).filter(Filme.titulo == titulo).update(
                {"ano": ano}
            )
            db.session.commit()
