from fastapi import APIRouter

users = APIRouter()

@users.get("/users")
def get_users():
    return {"Hello": "Users"}

@users.post("/users")
def create_user():
    return {"Hello": "Users"}

