from schemas.User import UserLogin
from fastapi import HTTPException
from config.db import conn
from controllers.user import decodePwd

def checkUser(user: UserLogin):
    with conn.cursor() as cursor:
        sql = "SELECT * FROM users WHERE email = %s"
        cursor.execute(sql, (user.email))
        result = cursor.fetchone()    
    if decodePwd(result['password']) == user.password: return True

