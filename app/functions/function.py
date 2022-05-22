import os
from csv import DictReader
import pandas as pd
from datetime import date
import smtplib


PATH = os.getenv("FILEPATH")
EMAILS = os.getenv("EMAILS")
TEXT = os.getenv("TEXT")

def read_archive():
    data = []
    file = pd.read_excel(PATH)
    for i, row in file.iterrows():
        data.append(str(row))
    return data


def choose_table():
    falta_promessa = []
    promessa_n_atende = []
    promessa_a_vencer = []
    promessa_vencida = []
    normal = []

    file = pd.read_excel(PATH)

    #   file['ISSUE DATE'] = pd.to_datetime(file['ISSUE DATE'])
    #   file['PROM SHIP DATE'] = pd.to_datetime(file['PROM SHIP DATE'], format='%Y.%m.%d')
    #   file['REQUESTED DATE'] = pd.to_datetime(file['REQUESTED DATE'], format='%Y.%m.%d')

    """day = date.today()
    weekday = date.today().weekday()
    day = pd.to_datetime(day)
    day2 = (day + pd.DateOffset(days = 2))
    print(day2)
    for i, row in file.iterrows():
        if pd.isna(row['PROM SHIP DATE']):
            falta_promessa.append(str(row))
        elif row['REQUESTED DATE'] < row['PROM SHIP DATE']:
            print('entrou cond 2')
            promessa_n_atende.append(str(row))
        elif row['PROM SHIP DATE'] == day2:
            print('entrou condiçao 3')
            promessa_a_vencer.append(str(row))
        elif row['PROM SHIP DATE'] < day:
            promessa_vencida.append(str(row))
        else:
            print('normal')
            normal.append(str(row))
    """
    return file

def emails():
    email = pd.read_csv(EMAILS, sep=" ",header=None)
    text = "Querido Carlos,\n\n Isto é uma mensagem de teste.\nTenha um bom fim-de-semana.\n\n Cumprimentos."
    return text, email

