from src.infra.configs import Base
from sqlalchemy import Column, String, Integer


class Filme(Base):
    __tablename__ = "filmes"

    titulo = Column(String, primary_key=True)
    genero = Column(String, nullable=False)
    ano = Column(Integer, nullable=False)

    def __repr__(self):
        return (
            f"""Filme(titulo={self.titulo}"""
            """, genero={self.genero}, ano={self.ano})"""
        )
