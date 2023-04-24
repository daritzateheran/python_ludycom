from fastapi import FastAPI
from routes.users import users
from routes.login import login
from routes.transactions import transactions

app = FastAPI()
app.include_router(users)
app.include_router(login)
app.include_router(transactions)

@app.get("/")
def read_root():
    return {"Hello": "World"}