#!/usr/bin/env python3
# made by prince kumar 
# date 1  mar 2022
# import all the stuff 
from email import header
from lib2to3.pgen2 import token
from unittest import result
from aiohttp import request
import requests 
import json 
Token = input("\033[32;1m Enter the api for your bot : ")
url = f"https://api.telegram.org/bot{Token}/getUpdates"

req = requests.post(url)
data = req.json()
chatId = data["result"][0]["message"]["chat"]["id"]

## nowsend the sms
sms = input("\033[36;1m Enter the msg : ")
num = input("\033[35;1m Enter the amount: ")

senUrl = f"https://api.telegram.org/bot{Token}/sendMessage?chat_id={chatId}&text={sms}"
for i in range(int(num)):
    req = requests.get(senUrl)
    if req.status_code == 200:
        print(f"Sms sent {i+1}")
    else :
        pass



