from sqlalchemy import create_engine, Column, String, Integer
from sqlalchemy.orm import sessionmaker, declarative_base

# configs
engine = create_engine("mysql+pymysql://root:1234@localhost:3306/cinema")
Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()


# Entities
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

# SQL

# Insert
data_insert = Filme(titulo="Batman", genero="Drama", ano=2022)
session.add(data_insert)
session.commit()

# Delete
session.query(Filme).filter(Filme.titulo == "Batman").delete()
session.commit()

# update
session.query(Filme).filter(Filme.genero == "Drama").update({"ano": 2000})
session.commit()

# commit
session.close()

# SELECT
data = session.query(Filme).all()
print(data)
