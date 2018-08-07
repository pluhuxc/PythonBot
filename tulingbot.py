#!/usr/bin/env python3

import requests

API_KEY = ""


class tulingbot:
    '''simple tuling bot '''

    def __init__(self, API_KEY, USERID):
        self.API_KEY = API_KEY
        self.API_URL = "http://openapi.tuling123.com/openapi/api/v2"
        self.USERID = USERID

    def sendtext(self, msg):
        self.msg = str(msg)
        self.json_data = {
            "reqType":0,
            "perception":{
                "inputText":{
                    "text":self.msg
                    }
                },
            "userInfo": {
                "apiKey": self.API_KEY,
                "userId": self.USERID
                }
            }
        req = requests.post(self.API_URL, json=self.json_data)
        data = req.json()['results'][0]['values']['text']
        return data

    

# example

bot1 = tulingbot(API_KEY, "user1")
msg = str(input("ME: "))
bot_msg = bot1.sendtext(msg)
print("bot: ", bot_msg)
