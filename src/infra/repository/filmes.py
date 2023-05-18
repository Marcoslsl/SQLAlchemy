from src.infra.configs.connection import DBConnectionHandler
from src.infra.entities import Filmes
from sqlalchemy.orm.exc import NoResultFound


class FilmesRepo:
    def __init__(self, connectionHandler) -> None:
        self.__connectionHandler = connectionHandler

    def select(self):
        with self.__connectionHandler() as db:
            try:
                data = db.session.query(Filmes).all()
                return data
            except NoResultFound:
                raise None
            except Exception as e:
                db.session.rollback()
                raise e

    def insert(self, titulo, genero, ano):
        with self.__connectionHandler() as db:
            try:
                data_insert = Filmes(titulo=titulo, genero=genero, ano=ano)
                db.session.add(data_insert)
                db.session.commit()
                return data_insert
            except Exception as e:
                db.session.rollback()
                raise e

    def delete(self, titulo):
        with self.__connectionHandler() as db:
            try:
                db.session.query(Filmes).filter(
                    Filmes.titulo == titulo
                ).delete()
                db.session.commit()
            except Exception as e:
                db.session.rollback()
                raise e

    def update(self, titulo, ano):
        with self.__connectionHandler() as db:
            try:
                db.session.query(Filmes).filter(
                    Filmes.titulo == titulo
                ).update({"ano": ano})
                db.session.commit()
            except Exception as e:
                db.session.rollback()
                raise e
