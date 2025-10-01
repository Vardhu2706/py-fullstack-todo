from starlette import status

from ..routers.users import get_db, get_current_user
from ..main import app  
from ..models import Todos
from .utils import *

app.dependency_overrides[get_db] = override_get_db
app.dependency_overrides[get_current_user] = override_get_current_user

def test_return_user(test_user):
    response = client.get('/user')
    assert response.status_code == status.HTTP_200_OK
    
    assert response.json()['username'] == 'example'
    assert response.json()['email'] == 'example@example.com'
    assert response.json()['first_name'] == 'example'
    assert response.json()['last_name'] == 'user'
    assert response.json()['role'] == 'admin'
    assert response.json()['phone_number'] == '(111)-111-111'
    
def test_change_password_success(test_user):
    response = client.put('/user/password', json={'password': 'test1234', 'new_password': 'test123'})
    
    assert response.status_code == status.HTTP_204_NO_CONTENT

def test_change_password_invalid(test_user):
    response = client.put('/user/password', json={'password': 'test123', 'new_password': 'test123'})
    
    assert response.status_code == status.HTTP_401_UNAUTHORIZED
    
def test_change_phone_number_success(test_user):
    response = client.put("/user/phone-number/1234567898")
    assert response.status_code == status.HTTP_204_NO_CONTENT