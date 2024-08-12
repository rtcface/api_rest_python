from fastapi import FastAPI
from routers import users, auth
from fastapi.staticfiles import StaticFiles

app = FastAPI()

# Routers
app.include_router(auth.router)
app.include_router(users.router)
app.mount("/statics", StaticFiles(directory="statics"), name="static")

@app.get("/api")
def api():
    return {"url": "devcool.org"}
