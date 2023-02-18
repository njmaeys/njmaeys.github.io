import os

from code_challenge import code_challenge_data
from auth_code import etsy_auth_help
from auth_token import new_token

if __name__ == "__main__":

    print("\n### Code challenge ###")
    code_challenge = code_challenge_data()
    code_verifier_val = code_challenge.get("code_verifier")
    code_challenge_val = code_challenge.get("code_challenge")
    print("Code verifier:", code_verifier_val)
    print("Code challenge:", code_challenge_val)

    print("\n### Auth code ###")
    print("Code url:", etsy_auth_help(code_verifier_val)[0])
    code = input("\nEtsy code: ")

    print("\n### Auth token ###")
    auth_token = new_token(code, code_verifier_val)
    print("Access token:", auth_token.get("access_token"))
    print("Refresh token:", auth_token.get("refresh_token"))

