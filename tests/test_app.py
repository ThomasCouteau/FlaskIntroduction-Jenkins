import pytest
from app import app, db, Todo
from datetime import datetime

@pytest.fixture
def client():
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
    client = app.test_client()

    # Establish an application context before running the tests.
    ctx = app.app_context()
    ctx.push()

    # Create the database and the table.
    db.create_all()

    yield client

    # Teardown after tests are done.
    db.session.remove()
    db.drop_all()
    ctx.pop()

def test_index_get(client):
    """Test the index page route on GET request."""
    response = client.get('/')
    assert response.status_code == 200
    assert b'DOCTYPE html' in response.data
    assert b'Task Master' in response.data

def test_index_post(client):
    """Test the index page route on POST request with new task."""
    response = client.post('/', data={'content': 'Test task'}, follow_redirects=True)
    assert response.status_code == 200
    assert b'Test task' in response.data

def test_task_delete(client):
    """Test deleting a task."""
    # First, insert a dummy task.
    task = Todo(content='A task to delete')
    db.session.add(task)
    db.session.commit()

    response = client.get(f'/delete/{task.id}', follow_redirects=True)
    assert response.status_code == 200
    assert b'A task to delete' not in response.data

def test_task_update_get(client):
    """Test the GET request to the update page."""
    # First, insert a dummy task.
    task = Todo(content='Initial Content')
    db.session.add(task)
    db.session.commit()

    response = client.get(f'/update/{task.id}')
    assert response.status_code == 200
    assert b'Initial Content' in response.data

def test_task_update_post(client):
    """Test the POST request to update the task content."""
    # First, insert a dummy task.
    task = Todo(content='Before update')
    db.session.add(task)
    db.session.commit()

    response = client.post(f'/update/{task.id}', data={'content': 'After update'}, follow_redirects=True)
    assert response.status_code == 200
    assert b'After update' in response.data
    assert b'Before update' not in response.data
