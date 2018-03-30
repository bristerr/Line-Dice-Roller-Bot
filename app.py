import requests
import re
import random
import configparser
from bs4 import BeautifulSoup
from flask import Flask, request, abort
from imgurpython import ImgurClient
from random import randint
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
client_id = config['imgur_api']['Client_ID']
client_secret = config['imgur_api']['Client_Secret']
album_id = config['imgur_api']['Album_ID']
API_Get_Image = config['other_api']['API_Get_Image']


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

def DiceRoller():
    sms= "2 fives 5"
    num=[int(s) for s in sms.split() if s.isdigit()] #isolates numbers as set
    #from random import randint #RNG code
    repeat = 0
    dice = num[0]
    pips = num[1]
    content="Don't you mean the Orthodox Church?"
    return content
   # while (repeat < dice): #loop
        #roll=randint(1,pips)
        #repeat = repeat +1
        #content.append(roll)
        #if (repeat == dice):
            #return content

@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    print("event.reply_token:", event.reply_token)
    print("event.message.text:", event.message.text)
    if "Slavonic" in event.message.text:
        content = DiceRoller()
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text=content))
        return 0
    if event.message.text == "蘋果即時新聞":
        content = DiceRoller()
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text=content))
        return 0
if __name__ == '__main__':
    app.run()
