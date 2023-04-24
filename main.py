from fastapi import FastAPI
from routes.users import users

app = FastAPI()
app.include_router(users)

@app.get("/")
def read_root():
    return {"Hello": "World"}