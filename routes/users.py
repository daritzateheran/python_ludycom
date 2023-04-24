from fastapi import APIRouter
from schemas.User import User
from starlette.status import HTTP_200_OK
from controllers.user import *

users = APIRouter()

@users.post("/users", status_code=HTTP_200_OK)
def createUser(user: User):
    validateUser(user.email)
    user.password = hashPassword(user.password)
    insertUser(user)      
    return {"msg": "User created", "name": user.email}

@users.post("/logout")
def logout():
    return {"Hello": "Users"}