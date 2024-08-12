import base64
import requests
from dotenv import load_dotenv
import os
import requests

load_dotenv()

def raw_file2base64(raw_audio):
    return base64.b64encode(raw_audio).decode('utf-8')

def send_post_request(payload):
    url = "https://shazam.p.rapidapi.com/songs/v2/detect"
    querystring = {"locale":"en-US"}
    headers = {
        "x-rapidapi-key": os.getenv("RAPIDAPI_KEY"),
        "x-rapidapi-host": os.getenv("RAPIDAPI_HOST"),
        "Content-Type": "text/plain"
    }
    return requests.post(url, data=payload, headers=headers, params=querystring)

