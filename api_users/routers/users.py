from services.shared.users_service import (users_list,
    get_user_id,
    User,
    add_new_user,
    update_user,
    delete_user)
from schemas.user_schema import UserSchema

from models.user_connection import UserConnection

from fastapi import APIRouter

router = APIRouter(prefix="/users", responses={404: {"description": "Not found"}}, tags=["Users"])
# Database
conn = UserConnection()

@router.get("/")
async def get_users():
    return users_list 

@router.get("/{id}")
async def get_user(id: int):
    return get_user_id(id)

@router.get("/query/")
async def get_users_query(id:int):
    return get_user_id(id)
    return list(users)[0]

@router.post("/insert", status_code=201)
async def insert_user_db(user: UserSchema):
    conn.add_user(user.dict())
    return user

@router.delete("/{id}", status_code=200)
async def delete_user_db(id: int):
    return id

@router.put("/ubdate_db", status_code=200)
async def update_user_db(user: User, id: int):
    conn.update_user(user.dict())
    return user

@router.get("/users_db", status_code=200)
async def get_users_db():
    print("get_users_db")
    return {"users": conn.get_users()}



@router.post("/", status_code=201)
async def add_user(user: User):
    return add_new_user(user)

@router.put("/", status_code=200)
async def update( user: User):
    return update_user(user)

@router.delete("/{id}", status_code=200)
async def delete(id: int):
    return delete_user(id)
