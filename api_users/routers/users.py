from services.shared.users_service import (users_list,
    get_user_id,
    User,
    add_new_user,
    update_user,
    delete_user,
    add_user_db,
    bk_update_user_db,
    get_users_db,
    get_user_id_db,
    borrar_usuario_db)

from schemas.user_schema import UserSchema


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

@router.post("/insert", status_code=201)
async def insert_user_db(user: UserSchema):
    return add_user_db(user)

@router.delete("/{id}", status_code=200)
async def delete_user_db(id: int):
    return id

@router.put("/ubdate_db/{id}", status_code=200)
async def update_user_db(user: UserSchema, id: int):
    result = bk_update_user_db(user, id)
    return result

@router.get("/users_db/", status_code=200)
async def bk_users_db():
    print("get_users_db")
    return get_users_db()

@router.get("/users_db/{id}", status_code=200)
async def get_user_db(id:str):
    print(id)
    return get_user_id_db(id)



@router.post("/", status_code=201)
async def add_user(user: User):
    return add_new_user(user)

@router.put("/", status_code=200)
async def update( user: User):
    return update_user(user)

@router.delete("/{id}", status_code=200)
async def delete(id: int):
    return delete_user(id)

@router.delete("/users_db/{id}")
async def delete_udb(id: str):
    print("Routers",id)
    data = borrar_usuario_db(id)
    print("data Routers",data)
    return {"message": "User deleted", "data": data}


