from services.shared.users_service import (users_list,
    get_user_id,
    User,
    add_new_user,
    update_user,
    delete_user)

from fastapi import APIRouter

router = APIRouter(prefix="/users", responses={404: {"description": "Not found"}}, tags=["Users"])

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

@router.post("/", status_code=201)
async def add_user(user: User):
    return add_new_user(user)

@router.put("/", status_code=200)
async def update( user: User):
    return update_user(user)

@router.delete("/{id}", status_code=200)
async def delete(id: int):
    return delete_user(id)
