import os
from csv import DictReader
import pandas as pd
from datetime import datetime, timedelta
import smtplib
import json
import requests



PATH = os.getenv("FILEPATH")
EMAILS = os.getenv("EMAILS")
TEXT = os.getenv("TEXT")
PASSWORD = os.getenv("PASSWORD")
EMAIL = os.getenv("EMAIL")

promise_to_win = []
lack_promise = []
promise_not_answer = []
expired_promise = []
normal = []

def choose_table(a):
    link = 'https://projeto-cnhi-default-rtdb.firebaseio.com/'
    request = requests.get(f'{link}/.json')
    dic = request.json()

    day = pd.to_datetime(datetime.now())
    weekday = pd.to_datetime(datetime.now().weekday())

    for i in dic:
        for row in dic[i]:
            row["SHIP_DUE"] =  row.pop("SHIP DUE")
            row["LAST_UPDATED"] =  row.pop("Last Updated")

    for i in dic:
        for row in dic[i]:
            if 'PROMISE' not in row:
                #print('1')
                lack_promise.append(row)
            elif pd.to_datetime(row['SHIP_DUE']) < pd.to_datetime(row['PROMISE']):
                #print('2')
                promise_not_answer.append(row)
            elif pd.to_datetime(row['PROMISE']) == (day+timedelta(days=2 )):
                #print('3')
                promise_to_win.append(row)
            elif pd.to_datetime(row['PROMISE']) < day:
                #print('4')
                expired_promise.append(row)
            else:
                #print('5')
                normal.append(row)

    json_lack = json.dumps(lack_promise)
    json_not_answer = json.dumps(promise_not_answer)
    json_to_win = json.dumps(promise_to_win)
    json_expired = json.dumps(expired_promise)
    json_normal = json.dumps(normal)
    if a == 1: return json_lack
    if a == 2: return json_not_answer 
    if a == 3: return json_to_win
    if a == 4: return json_expired
    if a == 5: return json_normal

def emails():
    email = pd.read_csv(EMAILS, sep=" ",header=None)
    text = "Querido Carlos,\n\n Isto é uma mensagem de teste.\nTenha um bom fim-de-semana.\n\n Cumprimentos."
    return text, email

def lack():
    result = choose_table(1)
    return result

def awnser():
    result = choose_table(2)
    print(result)
    return result

def win():
    result = choose_table(3)
    return result

def expired():
    result = choose_table(4)
    return result

def normal():
    result = choose_table(5)
    return result

    

