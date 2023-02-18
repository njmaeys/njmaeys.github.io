import os
from requests_oauthlib import OAuth2Session

etsy_scope = ["listings_r"]

etsy_keystring = os.getenv("API_KEY")
callback_url = os.getenv("REDIRECT_URL")

def get_access_token(keystring, auth_code, code_verifier, redirect_url, scopes):
  
    headers = {
        "Accept": "application/json",
        "Content-Type": "application/x-www-form-urlencoded",
        "x-api-key": keystring,
    }
    oauth = OAuth2Session(
        keystring, redirect_uri=redirect_url, scope=scopes
    )
    token = oauth.fetch_token(
        "https://api.etsy.com/v3/public/oauth/token",
        code=auth_code,
        code_verifier=code_verifier,
        include_client_id=True,
        headers=headers,
    )
    return token
  

def new_token(etsy_auth_code, etsy_code_verifier):
    return get_access_token(etsy_keystring, etsy_auth_code, etsy_code_verifier, callback_url, etsy_scope)
