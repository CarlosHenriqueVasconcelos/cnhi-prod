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

def read_archive():
    data = []
    file = pd.read_excel(PATH)
    for i, row in file.iterrows():
        data.append(str(row))
    return data

def normalize_invoices(data):
    result = data.to_json(orient="records")
    parsed = json.loads(result)
    return parsed


def choose_table():
    link = 'https://projeto-cnhi-default-rtdb.firebaseio.com/'
    request = requests.get(f'{link}/.json')
    print(request)
    dic = request.json()
    promessa_n_atende = []
    promessa_a_vencer = []
    promessa_vencida = []
    normal = []
    falta_promessa = []
   
    '''for i in dic:
        dic[i]['SHIP DUE'] = pd.to_datetime(dic[i]['SHIP DUE'])
        dic[i]['PROMISE'] = pd.to_datetime(dic[i]['PROMISE'])
        dic[i]['Last Updated'] = pd.to_datetime(dic[i]['Last Updated'])
    '''
    day = pd.to_datetime(datetime.now())
    weekday = pd.to_datetime(datetime.now().weekday())

    for i in dic:
        for row in dic[i]:
            if 'PROMISE' not in row:
                print('1')
                falta_promessa.append(row)
            elif pd.to_datetime(row['SHIP DUE']) < pd.to_datetime(row['PROMISE']):
                print('2')
                promessa_n_atende.append(row)
            elif pd.to_datetime(row['PROMISE']) == (day+timedelta(days=2 )):
                print('3')
                promessa_a_vencer.append(row)
            elif pd.to_datetime(row['PROMISE']) < day:
                print('4')
                promessa_vencida.append(row)
            else:
                print('5')
                normal.append(row)
    return falta_promessa

def emails():
    email = pd.read_csv(EMAILS, sep=" ",header=None)
    text = "Querido Carlos,\n\n Isto é uma mensagem de teste.\nTenha um bom fim-de-semana.\n\n Cumprimentos."
    return text, email

def data_base():
    link = 'https://projeto-cnhi-default-rtdb.firebaseio.com/'
    request = requests.get(f'{link}/.json')
    print(request)
    dic = request.json()
    return dic
  

