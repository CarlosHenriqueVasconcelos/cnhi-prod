from flask import Flask
from http import HTTPStatus
from app.functions import function
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email import encoders
import smtplib
import json
from flask import jsonify

app = Flask(__name__)


@app.get("/all_table")
def read_all_table():
    result = function.choose_table(2)
    parsed = function.normalize_invoices(result)

    response = jsonify(parsed)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


@app.get("/success")
def success():
    result = function.choose_table(5)
    parsed = function.normalize_invoices(result)

    response = jsonify(parsed)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


@app.get("/Promessa_nao_atende")
def read_promessa():
    result = function.choose_table(2)
    print(type(result))
    parsed = function.normalize_invoices(result)

    response = jsonify(parsed)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.get("/Promessa_nao_atende")
def read_promessa():
    result = function.choose_table(1)
    print(type(result))
    parsed = function.normalize_invoices(result)

    response = jsonify(parsed)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.get("/Falta_de_promessa")
def read_promessa():
    result = function.choose_table(3)
    print(type(result))
    parsed = function.normalize_invoices(result)

    response = jsonify(parsed)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.get("/Promessa_Vencida")
def read_promessa():
    result = function.choose_table(4)
    print(type(result))
    parsed = function.normalize_invoices(result)

    response = jsonify(parsed)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


@app.get("/sent_mail")
def sent_email():
    My_Address ='carlos@fmloliveira.com'
    Passoword ='solrac22'
    text, email = function.emails()
    email2 = [email]
    print(My_Address)
    print(Passoword)

    msg = MIMEText(text, 'plain')
    msg['From']=My_Address
    msg['To']= '.join([‘cnhi@fmloliveira.com’])'
    msg['Subject']="This is TEST"
    raw = msg.as_string()

    s = smtplib.SMTP(host='smtp.gmail.com', port= 587)
    s.starttls()
    s.ehlo()
    s.login(My_Address, Passoword)

    smtp.sendmail(My_Address, email2, raw)
    smtp.quit()
    return {"TESTE": enviou}