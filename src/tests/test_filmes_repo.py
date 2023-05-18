from unittest import mock
from mock_alchemy.mocking import UnifiedAlchemyMagicMock
from src.infra.entities import Filmes
from src.infra.repository import FilmesRepo


class ConnectionHandlerMock:
    def __init__(self) -> None:
        self.session = UnifiedAlchemyMagicMock(
            data=[
                (
                    [
                        mock.call.query(Filmes),
                        # mock.call.filter(Filmes.genero == "acao")
                    ],
                    [Filmes(titulo="vingadores", genero="acao", ano=2012)],
                )
            ]
        )

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.session.close()


def test_select():
    film_repo = FilmesRepo(ConnectionHandlerMock)
    response = film_repo.select()
    assert isinstance(response, list)
    assert isinstance(response[0], Filmes)
    assert response[0].titulo == "vingadores"
    print(response)


def test_insert():
    film_repo = FilmesRepo(ConnectionHandlerMock)
    response = film_repo.insert("something", "aaa", 2014)
    print(response)
