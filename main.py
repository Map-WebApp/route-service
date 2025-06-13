
import os
from fastapi import FastAPI, HTTPException
from dotenv import load_dotenv
import googlemaps

load_dotenv()

app = FastAPI()
gmaps = googlemaps.Client(key=os.getenv("GOOGLE_MAPS_API_KEY"))

@app.get("/directions")
def get_directions(origin: str, destination: str):
    try:
        result = gmaps.directions(origin, destination, mode="driving")
        return result
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
