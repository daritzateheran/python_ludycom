from fastapi import APIRouter
from controllers.login import *
from auth.jwt import signJWT
from schemas.User import UserLogin


login = APIRouter()

@login.post("/login")
def loginUsers(user: UserLogin):
    if checkUser(user):
        return signJWT(user.email)
    return {
        "msg": "Wrong login details!"
    }

