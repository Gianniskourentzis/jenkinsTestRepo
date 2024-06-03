from fastapi import FastAPI, HTTPException
from dotenv import load_dotenv
import requests
import base64
import os
 
env_file_path = './app/.env' 
load_dotenv(dotenv_path=env_file_path) 

app = FastAPI()

def get_token(url, client_id, client_secret, mail, password):
    concatenated_string = f"{client_id}:{client_secret}" 
    base64_encoded_string = base64.b64encode(concatenated_string.encode()).decode() 

    headers = {
        "Authorization": "Basic " + base64_encoded_string,
        "Content-Type": "application/x-www-form-urlencoded",
        "Accept": "application/json"
    }

    data = {
        "username": mail, 
        "password": password,
        "grant_type": "password"
    }

    response = requests.post(url, headers=headers, data=data)

    if response.status_code == 200:
        return response.json()
    else:
        raise HTTPException(status_code=response.status_code, detail=response.text)

@app.post("/login")
async def read_item(mail: str, password: str):
    url = os.getenv('URL')
    client_id = os.getenv('CLIENT_ID')
    client_secret = os.getenv('CLIENT_SECRET') 

    token = get_token(url, client_id, client_secret, mail, password)
    return token