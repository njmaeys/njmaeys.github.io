import json
import os
import requests

from fastapi import FastAPI, HTTPException
from starlette.middleware.cors import CORSMiddleware


SHOP_ID=os.environ.get("SHOP_ID")
API_KEY=os.environ.get("API_KEY")
CODE_VERIFIER=os.environ.get("CODE_VERIFIER")


app = FastAPI()

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
    if not isinstance(data, list):
        return listings

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
def get_listings():
    TRY_COUNT=0

    # This would be much better done with a DB but a json file locally is good enough
    with open("token.json", "r") as tf:
        token_data = json.load(tf)

    resp = requests.get(
        f"https://openapi.etsy.com/v3/application/shops/{SHOP_ID}/listings?includes=Images",
        headers={
            "X-API-KEY": API_KEY,
            "Authorization": f"Bearer {token_data['access_token']}"
        },
    )

    if resp.status_code == 401:
        # Get a refresh token and call get_listings again
        if TRY_COUNT > 3:
            raise HTTPException(status_code=429, detail="Too many attempts")
        TRY_COUNT += 1

        payload = {
            "grant_type": "refresh_token",
            "client_id": API_KEY,
            "refresh_token": token_data['refresh_token'],
            "code_verifier": CODE_VERIFIER,
            "redirect_uri": "https://www.natemaeysfineart.com",
        }

        response = requests.post(
            "https://api.etsy.com/v3/public/oauth/token",
            json=payload,
        )

        with open('token.json', 'w') as outfile:
            json.dump(response.json(), outfile)

        get_listings()
    
    results = resp.json()
    listings = results.get("results", None)
    if not listings:
        # Get a refresh token and call get_listings again
        if TRY_COUNT > 3:
            raise HTTPException(status_code=429, detail="Too many attempts")
        TRY_COUNT += 1

        get_listings()

    listings = parse_listings(listings)
    if not listings:
        # Get a refresh token and call get_listings again
        if TRY_COUNT > 3:
            raise HTTPException(status_code=429, detail="Too many attempts")
        TRY_COUNT += 1

        get_listings()
    
    return listings
