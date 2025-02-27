from fastapi.testclient import TestClient

import pytest 

from flow_capture.views import app

@pytest.fixture(name="client")
def client_fixture():
    return TestClient(app)

def test_hello(client):
    """
    Root URL greets the world.
    """
    resp = client.get("/")

    assert 200 == resp.status_code
    assert { 
        'message': 'Hello World'
    } == resp.json()

