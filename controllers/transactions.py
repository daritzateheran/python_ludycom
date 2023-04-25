from schemas.Transaction import Transaction, TransactionDb
from config.db import conn
from fastapi import HTTPException
import os, requests

GEOAPIFY_API_KEY = os.environ["GEOAPIFY_API_KEY"]

def insertTransactions(t: Transaction):
    try:
        with conn.cursor() as cursor:
            sql = "INSERT INTO transactions (idUser, lat, lon, city, date) VALUES (%s, %s, %s, %s, %s)"
            cursor.execute(sql, (getIdUser(t.email), t.lat, t.lon, t.city, t.date))
            conn.commit()
    except:
        raise HTTPException(status_code=500, detail="Something were wrong") 
    
def getAll():
    try:
        with conn.cursor() as cursor:
            sql = "SELECT * FROM transactions"
            cursor.execute(sql)
            transactions = cursor.fetchall()
            return transactions
    except:
        raise HTTPException(status_code=500, detail="Something were wrong")
    

def getCoords(city: str):  
    try:
        urlCity = f"https://api.geoapify.com/v1/geocode/search?text={city}&apiKey={GEOAPIFY_API_KEY}"
        response = requests.get(urlCity).json()
        coords = response["features"][0]["geometry"]["coordinates"]
        return coords
    except:
        raise HTTPException(status_code=500, detail="Something were wrong with coords")
    
def getRestaurantsNames(lat: str, lon: str):
    try:
        urlRestaurants = f'https://api.geoapify.com/v2/places?categories=catering.restaurant&bias=proximity:{lat},{lon}&limit={20}&lang=es&apiKey={GEOAPIFY_API_KEY}'
        responseRestaurants = requests.get(urlRestaurants).json()
        names = [r['properties'].get('name', '') for r in responseRestaurants['features']]
        return names
    except:
        raise HTTPException(status_code=500, detail="Something were wrong with reaching restaurants")
    
def getIdUser(email):
    with conn.cursor() as cursor:
        sql = "SELECT * FROM users WHERE email = %s"
        cursor.execute(sql, (email))
        result = cursor.fetchone()
    if result: return result['id']