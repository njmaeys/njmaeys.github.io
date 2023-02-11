import os
import requests
import json

"""
Any time I add or sell listings I need to run this script and merge to main.
The API was way more work than I was willing to figure out with Oauth so this is
my dirty hack. The v2 is getting deprecated so at some point this will no
longer work.
"""

url = f"https://openapi.etsy.com/v2/shops/NateMaeysFineArt/listings/active?limit=100&includes=MainImage&fields=title,url,price&api_key={os.environ.get('ETSY_API_KEY')}"

results = requests.get(url)

clean_listings = []
for r in results.json()["results"]:
    clean_listings.append(
        {
            "url": r["url"],
            "title": r["title"],
            "price": r["price"],
            "image": r["MainImage"]["url_fullxfull"],
        }
    )

with open("listings.json", "w") as file:
    json.dump(clean_listings, file)

