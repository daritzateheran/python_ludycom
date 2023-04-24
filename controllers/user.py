from schemas.User import User
from config.db import conn
from cryptography.fernet import Fernet
from fastapi import HTTPException


key = Fernet.generate_key()
f = Fernet(key)

def validateUser(email):
    with conn.cursor() as cursor:
        sql = "SELECT * FROM users WHERE email = %s"
        cursor.execute(sql, (email))
        result = cursor.fetchone()
    if result: raise HTTPException(status_code=400, detail="User already exists") 

def hashPassword(pwd):
    try:
        #f.encrypt(pwd.encode("utf-8"))
        return pwd
    except:
        raise HTTPException(status_code=500, detail="Something were wrong")

def decodePwd(pwd):
    try:
        #f.decrypt(pwd)
        return pwd
    except:
        raise HTTPException(status_code=500, detail="Something were wrong")

def insertUser(user: User):
    try:
        with conn.cursor() as cursor:
            sql = "INSERT INTO users (name, email, password) VALUES (%s, %s, %s)"
            cursor.execute(sql, (user.name, user.email, user.password))
            conn.commit()
    except:
        raise HTTPException(status_code=500, detail="Something were wrong")
    

