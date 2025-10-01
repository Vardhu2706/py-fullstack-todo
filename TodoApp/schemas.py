from pydantic import BaseModel, Field

class CreateUserRequest(BaseModel):
    username: str
    email: str
    first_name: str
    last_name: str
    password: str
    role: str
    phone_number: str
    
    model_config = {
        "json_schema_extra": {
            "example": {
                "username": "vardhu",
                "email": "vardhu@email.com",
                "first_name": "vardhaman",
                "last_name": "Ayyagari",
                "password": "test1234",
                "role": "admin",
                "phone_number": "123456789"
            }            
        }
    }

class TodoRequest(BaseModel):
    title: str = Field(min_length=3)
    description: str = Field(min_length=3, max_length=100)
    priority: int = Field(gt=0, lt=6)
    complete: bool
    
    model_config = {
        "json_schema_extra": {
            "example": {
                "title": "Get groceries",
                "description": "Get groceries by Wednesday.",
                "priority": 5,
                "complete": False
            }
        }
    }
    
class Token(BaseModel):
    access_token: str
    token_type: str
    
class UserVerification(BaseModel):
    password: str
    new_password: str = Field(min_length=6)