from schemas.Transaction import Transaction
from config.db import conn
from cryptography.fernet import Fernet
from fastapi import HTTPException


def insertTransactions(t: Transaction):
    try:
        with conn.cursor() as cursor:
            sql = "INSERT INTO users (email, lat, lon, date) VALUES (%s, %s, %s)"
            cursor.execute(sql, (t.email, t.lat, t.lon, t.date))
            conn.commit()
    except:
        raise HTTPException(status_code=500, detail="Something were wrong")
    