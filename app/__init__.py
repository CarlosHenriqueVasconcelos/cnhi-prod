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
    json_result = json.dumps(result)
    return json_result


@app.get("/success")
def success():
    result = function.choose_table(5)
    json_result = json.dumps(result)
    return json_result


@app.get("/Promessa_nao_atende")
def read_promessa():
    result = function.choose_table(2)
    json_result = json.dumps(result)
    return json_result

@app.get("/Promessa_nao_aten")
def read_promessa2():
    result = function.choose_table(1)
    json_result = json.dumps(result)
    return json_result

@app.get("/Falta_de_promessa")
def read_promessa3():
    result = function.choose_table(3)
    json_result = json.dumps(result)
    return json_result

@app.get("/Promessa_Vencida")
def read_promessa4():
    result = function.choose_table(4)
    json_result = json.dumps(result)
    return json_result


@app.get("/sent_mail")
def sent_email():
    
    My_Address ='carlos@fmloliveira.com'
    Passoword ='solrac22'
    text, email = function.emails()
    email2 = [email]

    msg = MIMEMultipart() 
    msg['From']= My_Address
    msg['To']= 'gisele.garcia@cnhind.com '
    msg['Subject']="This is TEST"
    msg.attach(MIMEText('Testando', 'plain'))

    smtp = smtplib.SMTP(host='email-smtp.us-east-1.amazonaws.com', port= 587)
    smtp.starttls()
    smtp.ehlo()
    smtp.login('AKIAUQTLH574IAYUBG6M', 'BLL1kh+GXeKUmmsX+NqJlbBxQ/ZR41y44ai9Gp9kvV+J')

    smtp.send_message(msg)
    smtp.quit()
    return {"TESTE": 'enviou'}

@app.get("/teste")
def steste():
    result = function.choose_table()
    json_result = json.dumps(result)
    return json_result