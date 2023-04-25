from fastapi import APIRouter
from controllers.login import *
from auth.jwt import signJWT
from schemas.User import UserLogin


login = APIRouter()

@login.get("/login")
def loginUsers(user: UserLogin):
    if checkUser(user):
        return signJWT(user.email)
    return {
        "msg": "Wrong login details!"
    }

@login.get("/logout")
def logout():
    #Delete token
    return {
        "msg": "User loggued out"
    }

