from dotenv import load_dotenv
load_dotenv()

import os
import pytest
from app import app


# ---------------------------
# Flask Test Client
# ---------------------------
@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client


# ---------------------------
# API Headers Fixture
# ---------------------------
@pytest.fixture
def api_headers():
    return {
        "x-api-key": os.getenv("API_KEY")
    }