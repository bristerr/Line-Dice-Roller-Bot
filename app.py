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
 #set seed
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

def SiegeRoller(sms):
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
            if (0 < total < 3):
                month = 1
            elif (2 < total < 6):
                month = 2
            elif (5 < total < 9):
                month = 3
            elif (8 < total < 13):
                month = 4
            elif (12 < total < 17):
                month = 5 
            elif (16 < total < 21):
                month = 6
            elif (20 < total < 25):
                month = 7
            elif (24 < total < 29):
                month = 8
            elif (28 < total < 33):
                month = 9 
            elif (32 < total < 37):
                month = 10
            elif (36 < total < 41):
                month = 11
            elif (40 < total < 45):
                month = 12
            elif (44 < total < 50):
                month = 13
            elif (49 < total < 55):
                month = 14
            elif (54 < total < 60):
                month = 15
            elif (59 < total < 65):
                month = 16
            elif (64 < total < 69):
                month = 17
            elif (68 < total < 73):
                month = 18
            elif (72 < total < 76):
                month = 19
            elif (75 < total < 78):
                month = 20
            elif (77 < total < 80):
                month = 21 
            elif (79 < total < 82):
                month = 22
            elif (81 < total < 86):
                month = 23
            elif (85 < total < 89):
                month = 24
            elif (88 < total < 91):
                month = 25 
            elif (90 < total < 93):
                month = 26
            elif (92 < total < 95):
                month = 27
            elif (94 < total < 97):
                month = 28    
            elif (total == 97):
                month = 29
            elif (total == 98):
                month = 30
            elif (total == 99):
                month = 31
            elif (total == 100):
                month = 32    
            else:
                month = 0
            content+="] for a siege length of " + str(month) + " months."
    return content

def Anakin():
    anakin = ['I have failed you Anakin, I have failed you.', ' Don\'t lecture me Obi-Wan.', 'It\'s over Anakin. I have the high ground.', 'I should have known the Jedi were trying to take over.', 'I hate sand. It\'s course, rough and gets everywhere.', 'From my point of view the Jedi are evil.', 'This is where the fun begins.', 'I should have known the Jedi were trying to take over.', 'I have brought peace, justice and security to my new Empire.']
    content = random.choice(anakin)
    return content 

def Senate():
    senate = ['I am the senate.', 'No, NO, YOU WILL DIE!', '*Autistic screeching*', 'It\'s treason then.', 'Ironic. He could save others but not himself.', 'Power! UNLIMITED POWER!', 'Have you ever heard the tragedy of Darth Plagueis the Wise?']
    content = random.choice(senate)
    return content 

def Open():
    content = ' Iberia/Maghreb: \n Badajoz \n Almoravids \n Memelars \n Almohads \n Algeria \n Tunis \n \n Italy: \n Papacy \n Spoleto \n Verona \n Pisa \n Savoie \n Lombard Minors \n Milan (May split) \n \n German HRE:  \n Burgundy (HRE Duchy) \n Aquileia \n Lower Lorraine (Will likely split) \n Upper Lorraine (Will likely split) \n Holland \n Utrecht \n Frisia \n East Frisia \n Baden \n Swabia (Will Likely Split) \n Messian \n North March (Brandenburg) \n Bavaria (Will likely weaken) \n Nordheim \n \n France: \n French Minors \n Brittany \n \n British Isles: \n Scotland \n Munster \n Leinster \n Other Irish minors \n Welsh minors \n Mann \n \n Eastern/Central European Pagans: \n Pomerania \n Mecklenburg \n Prussia \n Prussian Minors \n Lithuania (Not really united, in reality a confederation of tribes) \n \n Eastern European Christians: \n Kievan Rus’ \n Poland \n Other Russian States except Novgorod \n Steppe/Caucuses: \n Cumans \n Bulgars \n Circassian minors \n \n Middle East:  \n Edessa \n Seljuks \n Tripoli \n Seljuk Vassals'
    return content


def Year():
    import datetime 
    start = datetime.date(2018, 11, 4)
    today = datetime.date.today()
    end_date = today- start
    year=end_date.days
    content = 1066 + year*2
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
    
    if ".rs" in event.message.text:
        sms = event.message.text
        content = SiegeRoller(sms)
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
    
    if event.message.text == ".open":
        content = Open()
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
