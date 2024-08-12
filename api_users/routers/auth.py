from services.shared.auth_service import login, userIsAuthorized, User
from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

router = APIRouter(prefix="/auth", tags=["Auth"])
oauth2 = OAuth2PasswordBearer(tokenUrl="/auth/login")

async def current_user(token: str = Depends(oauth2)):
    return userIsAuthorized(token)

@router.post("/login")
async def login_user(form: OAuth2PasswordRequestForm = Depends()):
    return login(form.username, form.password)


@router.get("/users/me")
async def read_users_me(user: User = Depends(current_user)):
    return user



