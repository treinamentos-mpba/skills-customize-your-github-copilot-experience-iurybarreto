import pytest
from fastapi.testclient import TestClient

from app import app, tasks


@pytest.fixture
def client():
    tasks.clear()
    with TestClient(app) as test_client:
        yield test_client
    tasks.clear()


def test_health_check_returns_ok(client):
    # TODO: Teste GET /health, o status HTTP e o JSON retornado.
    pass


def test_task_crud_flow(client):
    # TODO: Teste criação, listagem, consulta, atualização e remoção de uma tarefa.
    pass


def test_missing_task_returns_not_found(client):
    # TODO: Teste GET, PUT e DELETE usando um identificador inexistente.
    pass


def test_task_without_title_is_rejected(client):
    # TODO: Envie uma tarefa sem título e verifique a resposta de validação.
    pass
