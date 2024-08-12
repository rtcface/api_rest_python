from fastapi import FastAPI
from routers import users, auth
from fastapi.staticfiles import StaticFiles
from models.user_connection import UserConnection

app = FastAPI()

# Database
conn = UserConnection()

# Routers
app.include_router(auth.router)
app.include_router(users.router)
app.mount("/statics", StaticFiles(directory="statics"), name="static")

@app.get("/")
def root():
    conn
    return {"url": "devcool.org"}
