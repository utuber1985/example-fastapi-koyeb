from typing import Union

from fastapi import FastAPI

app = FastAPI()
from Connect import XTSConnect
import Exception as ex
root = "https://ttblaze.iifl.com"
# login store access token, feedtoken
# pos ord hold
# place order
# websocket stream (use access and feed tokens) 

@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


@app.get("/login/{api_key}/{api_secret}")
def login(api_key: str, api_secret: str):
    root = "https://ttblaze.iifl.com"
    XTS_int = XTSConnect(api_key, api_secret, "WebAPI", root)
    resp = XTS_int.interactive_login()
    print(resp.text)
    access_token = resp["result"]["token"]
    Client_ID = resp["result"]["userID"]
    isInvestor=resp["result"]["isInvestorClient"]    
    return {"access_token": access_token}
