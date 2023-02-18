import os
from authentication import AuthHelper

etsy_scope = ["listings_r"]
etsy_keystring = os.getenv("API_KEY")
callback_url = os.getenv("REDIRECT_URL")


def etsy_auth_help(etsy_code_verifier):
    etsy_auth = AuthHelper(etsy_keystring, callback_url, etsy_scope, etsy_code_verifier)
    return etsy_auth.get_auth_code()
