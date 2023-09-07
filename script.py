"""
Manual Steps
Step 1: Log into Spotify
Step 2: Grab a playlist
Step 3: Log into SoundCloud
Step 4: Create a new playlist
Step 5: Search for each song in the Spotify playlist
Step 6: Add the song to the SoundCloud playlist
"""

from dotenv import load_dotenv
import os
import base64
from requests import post
import json

load_dotenv()

client_id = os.getenv("CLIENT_ID")
client_secret = os.getenv("CLIENT_SECRET")

print(client_id, client_secret)

def get_token():
    auth_string = client_id + ":" + client_secret
    auth_bytes = auth_string.encode("utf-8")
    auth_base64 = str(base64.b64encode(auth_bytes), "utf-8")

    url = "https://accounts.spotify.com/api/token"
    headers = {
        "Authorization": "Basic " + auth_base64,
        "Content-Type": "application/x-www-form-urlencoded"
    }
    data = {"grant_type": "client_credentials"}
    result = post(url, data=data, headers=headers)
    json_result = json.loads(result.content)
    token = json_result["access_token"]
    return token

token = get_token()
print(token)