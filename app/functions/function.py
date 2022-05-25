import os
from csv import DictReader
import pandas as pd
from datetime import datetime, timedelta
import smtplib
import json


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


def choose_table(choose):

    promessa_n_atende = []
    promessa_a_vencer = []
    promessa_vencida = []
    normal = []
    falta_promessa = []
   
    file = pd.read_excel(PATH)
 
    file['ISSUE DATE'] = pd.to_datetime(file['ISSUE DATE'])
    file['PROM SHIP DATE'] = pd.to_datetime(file['PROM SHIP DATE'])
    file['REQUESTED DATE'] = pd.to_datetime(file['REQUESTED DATE'], format='%Y.%m.%d')

    day = pd.to_datetime(datetime.now())
    weekday = pd.to_datetime(datetime.now().weekday())
  
    for i, row in file.iterrows():
        if pd.isna(row['PROM SHIP DATE']):
            #print('1')
            falta_promessa.append(row)
        elif row['REQUESTED DATE'] < row['PROM SHIP DATE']:
            #print('2')
            promessa_n_atende.append(row)
        elif row['PROM SHIP DATE'] == (day+timedelta(days=2 )):
            #print('3')
            promessa_a_vencer.append(row)
        elif row['PROM SHIP DATE'] < day:
            #print('4')
            promessa_vencida.append(row)
        else:
            #print('5')
            normal.append(row)
        
    promessa_n = pd.DataFrame(promessa_n_atende)
    falta_p = pd.DataFrame(falta_promessa)
    vencer = pd.DataFrame(promessa_a_vencer)
    vencida = pd.DataFrame(promessa_vencida)
    normal = pd.DataFrame(normal)
    
    
    if choose == 1: return promessa_n
    elif choose == 2: return falta_p
    elif choose == 3: return vencer
    elif choose == 4: return vencida
    else: return normal
    

def emails():
    email = pd.read_csv(EMAILS, sep=" ",header=None)
    text = "Querido Carlos,\n\n Isto é uma mensagem de teste.\nTenha um bom fim-de-semana.\n\n Cumprimentos."
    return text, email

