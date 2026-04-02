import pytest

from app import app


@pytest.fixture
def api_secret_key():
    return "test-secret-key"


@pytest.fixture
def auth_headers(api_secret_key):
    return {"X-API-KEY": api_secret_key}


@pytest.fixture
def client(api_secret_key):
    app.config.update(
        TESTING=True,
        API_SECRET_KEY=api_secret_key,
    )

    with app.test_client() as test_client:
        yield test_client
