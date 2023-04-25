from fastapi import APIRouter
from fastapi import Depends, HTTPException
from controllers.transactions import *
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from auth.jwt import decodeJWT
from datetime import datetime
import os

security = HTTPBearer()
transactions = APIRouter()
GEOAPIFY_API_KEY = os.environ["GEOAPIFY_API_KEY"]


@transactions.get("/getRestaurants/{city}")
def getRestaurants(city: str, credentials: HTTPAuthorizationCredentials = Depends(security)):
    try:
        payload = decodeJWT(credentials.credentials)
        if not payload: raise HTTPException(status_code=401, detail="Invalid Token")
        coords = getCoords(city)
        lat = coords[0]
        lon = coords[1]
        names = getRestaurantsNames(lat, lon)
        transaction = Transaction(
            email=payload['email'],
            lat=lat,
            lon=-lon,
            date=datetime.now().isoformat(),
            city=city
        )
        insertTransactions(transaction)
        return {"Near restaurants": names, "email": payload['email']}
    except HTTPException as e:
        raise e

@transactions.get("/historic")
def getHistoric(credentials: HTTPAuthorizationCredentials = Depends(security)):
    try:
        payload = decodeJWT(credentials.credentials)
        if not payload: raise HTTPException(status_code=401, detail="Invalid Token")
        return {"Transations": getAll(), "email": payload['email']}
    except HTTPException as e:
        raise e