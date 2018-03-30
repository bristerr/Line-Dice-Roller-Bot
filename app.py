
# coding: utf-8

# In[ ]:


import requests
import re
import random
import configparser
from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import *

app = Flask(__name__)
config = configparser.ConfigParser()
config.read("config.ini")

line_bot_api = LineBotApi(config['line_bot']['Channel_Access_Token'])
handler = WebhookHandler(config['line_bot']['Channel_Secret'])


@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    # print("body:",body)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 'ok'

def DiceRoller(sms):    
    num=[int(s) for s in sms.split() if s.isdigit()] #isolates numbers as set
    from random import randint #RNG code
    repeat = 0
    dice = num[0]
    pips = num[1]
    while (repeat < dice): #loop
        print("You rolled",randint(1,pips))
        repeat = repeat +1
    return    
   
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    if ".d" in event.message.text:
        content = DiceRoller(event.message.text)
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text=content))
        return 0

if __name__ == "__main__":
    app.run()

