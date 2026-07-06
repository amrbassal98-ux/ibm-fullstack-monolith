import pytest
from myserver import app, data_store

@pytest.fixture
def client():
    """Configures the app for testing and provides a test client."""
    app.config['TESTING'] = True
    with app.test_client() as client:
        # Reset global data_store for each test to maintain isolation
        data_store.clear()
        yield client

def test_hello_world(client):
    """Tests the root endpoint returns the correct welcome message."""
    response = client.get('/')
    assert response.status_code == 200
    assert response.data.decode('utf-8') == "Hello, World!"

def test_get_items_empty(client):
    """Tests GET /items returns an empty list when no items exist."""
    response = client.get('/items')
    assert response.status_code == 200
    assert response.get_json() == []

def test_add_item_success(client):
    """Tests POST /items successfully adds a new item."""
    response = client.post('/items', json={'item': 'flask_test'})
    assert response.status_code == 201
    assert response.get_json()['data'] == 'flask_test'
    assert 'flask_test' in data_store

def test_add_item_failure(client):
    """Tests POST /items returns 400 when the 'item' key is missing."""
    response = client.post('/items', json={})
    assert response.status_code == 400
    assert 'error' in response.get_json()

def test_update_item_success(client):
    """Tests PUT /items/<index> updates an existing item."""
    data_store.append('old_item')
    response = client.put('/items/0', json={'item': 'new_item'})
    assert response.status_code == 200
    assert response.get_json()['data'] == 'new_item'
    assert data_store[0] == 'new_item'

def test_update_item_not_found(client):
    """Tests PUT /items/<index> returns 404 for an out-of-range index."""
    response = client.put('/items/10', json={'item': 'ghost'})
    assert response.status_code == 404

def test_delete_item_success(client):
    """Tests DELETE /items/<index> removes the item."""
    data_store.append('delete_me')
    response = client.delete('/items/0')
    assert response.status_code == 200
    assert response.get_json()['data'] == 'delete_me'
    assert len(data_store) == 0

def test_delete_item_not_found(client):
    """Tests DELETE /items/<index> returns 404 for an out-of-range index."""
    response = client.delete('/items/10')
    assert response.status_code == 404