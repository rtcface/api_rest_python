from pydantic import BaseModel
from fastapi import HTTPException

from models.user_connection import UserConnection
# Database
conn = UserConnection()

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

# Funciones con la base de datos

# Insertar usuario
def add_user_db(user: User):
    conn.add_user(user.dict())
    return user
# Actualizar usuario
def bk_update_user_db(user: User, id: int):
    conn.update_user(user.dict(), id)
    return user
# Eliminar usuario
# Obtener usuarios
def get_users_db():
    print("get_users_db")
    items = []
    for user in conn.get_users():
        dictionary = {}
        dictionary["id"] = user[0]
        dictionary["name"] = user[1]
        dictionary["phone"] = user[2]
        items.append(dictionary)
    return {"users": items}
# Obtener usuario por id

def get_user_id_db(id):
    data = conn.get_user_db(id)
    if data == None:
        return {"message": "User not found"}
    
    dictionary = {}
    dictionary["id"] = data[0]
    dictionary["name"] = data[1]
    dictionary["phone"] = data[2]
    return {"user": dictionary}

def borrar_usuario_db(id):
    conn.bk_delete_user_db(id)
    return "delete_user_db"
