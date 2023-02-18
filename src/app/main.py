import os
import requests

from fastapi import FastAPI, HTTPException
from starlette.middleware.cors import CORSMiddleware


SHOP_ID=os.environ.get("SHOP_ID")
API_KEY=os.environ.get("API_KEY")
ACCESS_TOKEN=os.environ.get("ACCESS_TOKEN")
REFRESH_TOKEN=os.environ.get("REFRESH_TOKEN")
CODE_VERIFIER=os.environ.get("CODE_VERIFIER")

app = FastAPI()

#uvicorn main:app --port 80 --reload
origins = [
    # NOTE: This is bad but I give up
    "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def parse_listings(data):
    listings = []
    for d in data:
        # TODO: Parse through some day and get each image for display on my site.
        # For now just use the first one.
        listings.append(
            {
                "url": d["url"],
                "title": d["title"],
                "image": d["images"][0]["url_fullxfull"]
            }
        )
    
    return listings



@app.get("/listings")
async def get_listings():
    _access_token = ACCESS_TOKEN
    resp = requests.get(
        f"https://openapi.etsy.com/v3/application/shops/{SHOP_ID}/listings?includes=Images",
        headers={
            "X-API-KEY": API_KEY,
            "Authorization": f"Bearer {_access_token}"
        },
    )

    # Get a refresh token and call get_listings again
    try_count = 0
    if not resp.json()["results"]:
        print("\n### HERE ###")
        print(resp.json())
        #if try_count > 3:
        #    raise HTTPException(status_code=429, detail="Too many attempts")
        #try_count += 1

        #payload = {
        #    "grant_type": "refresh_token",
        #    "client_id": API_KEY,
        #    "refresh_token": REFRESH_TOKEN,
        #    "code_verifier": CODE_VERIFIER,
        #    "redirect_uri": "https://www.natemaeysfineart.com",
        #}

        #response = requests.post(
        #    "https://api.etsy.com/v3/public/oauth/token",
        #    json=payload,
        #)
        #_access_token = response.json().get("access_token")
        #get_listings()

    return parse_listings(resp.json()["results"])