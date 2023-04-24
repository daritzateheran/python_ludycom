from fastapi import APIRouter
from controllers.login import *
from controllers.jwt import *
from schemas.User import UserLogin


login = APIRouter()

@login.post("/login")
def loginUsers(user: UserLogin):
    if checkUser(user):
        return signJWT(user.email)
    return {
        "error": "Wrong login details!"
    }

