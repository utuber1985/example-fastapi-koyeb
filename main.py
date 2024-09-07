from typing import Union

from fastapi import FastAPI

app = FastAPI()
from Connect import XTSConnect
import Exception as ex
root = "https://ttblaze.iifl.com"
access_token=""
# login store access token, feedtoken
# pos ord hold
# place order
# websocket stream (use access and feed tokens) 

@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/margin")
def get_margin():
    global XTS_int
    str_margin=XTS_int.get_balance()
    return {"Margin": str_margin}

@app.get("/profile")
def get_profile():
    global XTS_int
    str_profile=XTS_int.get_balance()
    return {"Margin": str_profile}

@app.get("/login/{api_key}/{api_secret}")
def login(api_key: str, api_secret: str):
    global XTS_int
    root = "https://ttblaze.iifl.com"
    access_token="Check api key secret or try again"
    print(api_key,api_secret,root)
    try:
        XTS_int = XTSConnect(api_key, api_secret, "WebAPI", root)
        resp = XTS_int.interactive_login()
        print(resp)
        access_token = resp["result"]["token"]
        Client_ID = resp["result"]["userID"]
        isInvestor=resp["result"]["isInvestorClient"]    
    except Exception as ex:
        print(f'Error in token generation: {str(ex)}')
    return {"access_token": access_token}
