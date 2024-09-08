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
    str_profile=XTS_int.get_profile()
    return {"Margin": str_profile}

@app.get("/logout")
def get_logout():
    global XTS_int
    str_logout=XTS_int.interactive_logout()
    return {"Logout Sts": str_logout}

@app.get("/orders")
def get_orders():
    global XTS_int
    str_orders=XTS_int.get_order_book()
    return {"Orders": str_orders}

@app.get("/trades")
def get_trades():
    global XTS_int
    str_trades=XTS_int.get_trade()
    return {"Orders": str_trades}
    
@app.get("/holding")
def get_holding():
    global XTS_int
    str_holding=XTS_int.get_holding()
    return {"Orders": str_holding}

@app.get("/positions_day")
def get_pos_day():
    global XTS_int
    str_pos_day=XTS_int.get_position_daywise()
    return {"Positions (Daywise)": str_pos_day}

@app.get("/positions_net")
def get_pos_net():
    global XTS_int
    str_pos_net=XTS_int.get_position_netwise()
    return {"Positions (Netwise)": str_pos_net}

# Marketdata login
# get quote
# get hsitorical
# web socket


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

@app.get("/set_token/{access_token}")
def login(access_token: str):
    global XTS_int
    root = "https://ttblaze.iifl.com"
    api_key="apikey"
    api_secret="apisecret"
    user_id="user_id"
    status='fail'
    try:
        XTS_int = XTSConnect(api_key, api_secret, "WebAPI", root)
        resp = XTS_int.set_common_variables(user_id,access_token,True)
        status=resp['description']   
    except Exception as ex:
        print(f'Error in token generation: {str(ex)}')
    return {"Token Status": status}
