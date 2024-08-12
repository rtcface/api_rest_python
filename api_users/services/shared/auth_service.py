from passlib.context import CryptContext
from pydantic import BaseModel
from .users_db import users_db
from fastapi import HTTPException, status
from datetime import datetime, timedelta
import jwt
from jwt.exceptions import InvalidTokenError

SECRET_KEY = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 1

crypt = CryptContext(schemes=["bcrypt"], deprecated="auto")

class User(BaseModel):
    username: str
    full_name: str
    email: str
    disabled: bool

class UserDB(User):
    password: str

def userExists(username: str):
    if username in users_db:
        return User(**users_db[username])
    return False

def userIsAuthorized(token: str):
    try:
        print(token)
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        print(payload)
        username = payload.get("username")

        user = userExists(username)
        if not user:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="credentials is invalid",
                headers={"WWW-Authenticate": "Bearer"},
            )
        if user.disabled:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="user is disabled",
                headers={"WWW-Authenticate": "Bearer"},
            )
        return user
    except:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Super>>>credentials is invalid",
            headers={"WWW-Authenticate": "Bearer"},
        )

   #user = userExists(token)
   #if not user:
   #    raise HTTPException(
   #    status_code=status.HTTP_401_UNAUTHORIZED,
   #    detail="credentials is invalid",
   #        headers={"WWW-Authenticate": "Bearer"},
   #    )
   #if user.disabled:
   #    raise HTTPException(
   #        status_code=status.HTTP_401_UNAUTHORIZED,
   #        detail="user is disabled",
   #        headers={"WWW-Authenticate": "Bearer"},
   #    )
   #return user

def search_user(username: str):
    if username in users_db:
        return UserDB(**users_db[username])
    raise HTTPException(status_code=404, detail="User not found")

def login(username: str, password: str):
    user = search_user(username)
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    if crypt.verify(password, user.password):
        access_token = jwt.encode({"username": user.username, "exp": expire}, SECRET_KEY, algorithm=ALGORITHM)
        return {"access_token": access_token, "token_type": "bearer"}
    raise HTTPException(status_code=401, detail="Incorrect username or password")

def register(user: User):
    if user.username in users_db:
        return {"message": "User already exists"}
    users_db[user.username] = user.dict()
    return user

def logout(token: str):
    return {"message": "Logged out"}



