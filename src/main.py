import os
from dotenv import load_dotenv
import base64
from requests import post
import json

load_dotenv()
client_id = os.getenv("CLIENT_ID")
client_secret = os.getenv("CLIENT_SECRET")

def get_token():
    auth_str = client_id + ":" + client_secret
    auth_bytes = auth_str.encode("utf-8")
    auth_base64 = str(base64.b64encode(auth_bytes), "utf-8")

    url = "https://accounts.spotify.com/api/token"
    headers = {
        "Authorization": "Basic " + auth_base64,
        "Content-Type": "application/x-www-form-urlencoded"
    }

    data = {"grant_type": "client_credentials"}
    result = post(url, headers=headers, data=data)
    json_result = json.loads(result.content)
    
    json_formatted_str = json.dumps(json_result, indent=2)
    print(json_formatted_str)

    token = json_result["access_token"]
    return token

def get_client(token):
    token = get_token()

    url = "https://api.spotify.com/v1/me/player"
    headers = {
        "Authorization": "Bearer " + token
    }
    result = get

# print(token)