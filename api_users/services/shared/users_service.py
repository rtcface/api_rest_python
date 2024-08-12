from pydantic import BaseModel
from fastapi import HTTPException

class User(BaseModel):
    id: int
    name: str
    surname: str
    email: str
    age: int

users_list = [
    User(id=1,name="John", surname="Doe", email="john@doe.com", age=25),
    User(id=2,name="Jane", surname="Doe", email="jane@doe.com", age=30),
    User(id=3,name="Bob", surname="Doe", email="bob@doe.com", age=35),
    User(id=4,name="Alice", surname="Doe", email="alice@doe.com", age=40),
]
# Get user by id
def get_user_id(id: int):
    users = filter(lambda user: user.id == id, users_list)
    try:
        return list(users)[0]
    except IndexError:
        return ""
# Add user
def add_new_user(user: User):
    http_exception = HTTPException(status_code=400, detail="User already exists")
    if get_user_id(user.id) != "":
        raise http_exception
    users_list.append(user)
    return user
# Delete user
def delete_user(id: int):
    user = get_user_id(id)
    if user == "":
        return {"message": "User not found"} 
    users_list.remove(user)
    return user
# Update user
def update_user(user: User):
    user_update = get_user_id(user.id)
    
    if user_update == "":
        return {"message": "User not found"}
    user_update.name = user.name
    user_update.surname = user.surname
    user_update.email = user.email
    user_update.age = user.age
    return user_update


