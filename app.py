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

def DiceRoller(sms):
    num=[int(s) for s in sms.split() if s.isdigit()] #isolates numbers as set
    #from random import randint #RNG code
    repeat = 0
    dice = num[0]
    pips = num[1]
    content="You rolled ["
    value = []
    while (repeat < dice): #loop
        roll=randint(1,pips)
        repeat = repeat +1
        value.append(roll)
        if (repeat != dice):
            content+=str(roll) + ", "
        else: 
            content+=str(roll)   
        if (repeat == dice):
            total = sum(value)
            content+="] for a total of [" + str(total) + "]."   
    return content

def Anakin():
    anakin = ['I have failed you Anakin, I have failed you.', ' Don\'t lecture me Obi-Wan.', 'It\'s over Anakin. I have the high ground.', 'I should have known the Jedi were trying to take over.', 'I hate sand. It\'s course, rough and gets everywhere.', 'From my point of view the Jedi are evil.', 'This is where the fun begins.', 'I should have known the Jedi were trying to take over.', 'I have brought peace, justice and security to my new Empire.']
    content = random.choice(anakin)
    return content 

def Senate():
    senate = ['I am the senate.', 'No, NO, YOU WILL DIE!', '*Autistic screeching*', 'It\'s treason then.', 'Ironic. He could save others but not himself.', 'Power! UNLIMITED POWER!', 'Have you ever heard the tragedy of Darth Plagueis the Wise?']
    content = random.choice(senate)
    return content 

def Year():
    import datetime 
    start = datetime.date(2018, 3, 31)
    today = datetime.date.today()
    end_date = today- start
    year=end_date.days
    content = 1533 + year
    return content

@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    print("event.reply_token:", event.reply_token)
    print("event.message.text:", event.message.text)
    if ".d" in event.message.text:
        sms = event.message.text
        content = DiceRoller(sms)
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text=content))
        return 0
    
    if event.message.text == "anakin":
        content = Anakin()
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text=content))
        return 0
    
    if event.message.text == "senate":
        content = Senate()
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text=content))
        return 0
    
    if "the year" in event.message.text:
        content = Year()
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text=content))
        return 0
    
    if "year is it" in event.message.text:
        content = Year()
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text=content))
        return 0
    if "what year" in event.message.text:
        content = Year()
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text=content))
        return 0
    
if __name__ == '__main__':
    app.run()
