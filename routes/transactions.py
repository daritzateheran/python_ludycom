from fastapi import APIRouter
from fastapi import Depends, HTTPException
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from controllers.jwt import decodeJWT
import os, requests

security = HTTPBearer()
transactions = APIRouter()
GEOAPIFY_API_KEY = os.environ["GEOAPIFY_API_KEY"]


@transactions.get("/getRestaurants/{city}")
def getRestaurants(city: str, credentials: HTTPAuthorizationCredentials = Depends(security)):
    urlCity = f"https://api.geoapify.com/v1/geocode/search?text={city}&apiKey={GEOAPIFY_API_KEY}"
    response = requests.get(urlCity).json()
    coords = response["features"][0]["geometry"]["coordinates"]
    lat = coords[0]
    lon = coords[1]
    urlRestaurants = f'https://api.geoapify.com/v2/places?categories=catering.restaurant&bias=proximity:{lat},{lon}&limit={10}&lang=es&apiKey={GEOAPIFY_API_KEY}'
    #urlRestaurants = f"https://api.geoapify.com/v2/places/catering.restaurant?lat={lat}&lon={lon}&radius=5000&limit=10&apiKey={}"
    responseRestaurants = requests.get(urlRestaurants).json()
    print(len(responseRestaurants["features"]))


    try:
        payload = decodeJWT(credentials.credentials)
        return {"msg": "This is a protected route", "payload": payload}
    except HTTPException as e:
        raise e