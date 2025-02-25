import pytest
import json
from src.app import app  # Importación corregida

@pytest.fixture
def client():
    return app.test_client()

# Test para GET /members
def test_get_members_exist(client):
    response = client.get('/members')
    assert response.status_code == 200
    assert isinstance(json.loads(response.data), list)

# Test para GET /member/<id>
def test_get_single_member_implemented(client):
    response = client.get('/member/1')
    assert response.status_code == 200
    assert "first_name" in json.loads(response.data)

# Test para POST /member
def test_add_member(client):
    new_member = {
        "first_name": "Tommy",
        "age": 23,
        "lucky_numbers": [34, 65, 23, 4, 6]
    }
    response = client.post('/member', json=new_member)
    assert response.status_code == 200
    assert json.loads(response.data)["msg"] == "Member added successfully"

# Test para DELETE /member/<id>
def test_delete_member(client):
    response = client.delete('/member/1')
    assert response.status_code == 200
    assert json.loads(response.data)["done"] == True
