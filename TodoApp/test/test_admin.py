from starlette import status

from ..routers.admin import get_db, get_current_user
from ..main import app  
from ..models import Todos
from .utils import *

app.dependency_overrides[get_db] = override_get_db
app.dependency_overrides[get_current_user] = override_get_current_user

def test_admin_read_all_authenticated(test_todo):
    response = client.get("/admin/todo")
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == [{
        'title' : 'Learn to code',
        'description' : 'Need to learn everyday!',
        'priority' : 5,
        'complete' : False,
        'owner_id' : 1,
        'id': 1
    }]

def test_admin_delete_todos(test_todo):
    response = client.delete("/todo/1")
    assert response.status_code == status.HTTP_204_NO_CONTENT
    
    db = TestingSessionLocal()
    model = db.query(Todos).filter(Todos.id==1).first()
    
    assert model is None
    
def test_admin_delete_todos_not_found(test_todo):
    response = client.delete("/todo/999")
    assert response.status_code == status.HTTP_404_NOT_FOUND
    assert response.json() ==  {"detail":"Todo with ID '999' not found"}