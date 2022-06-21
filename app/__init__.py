from flask import Flask
from http import HTTPStatus
from app.functions import function
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email import encoders
import smtplib 
import json
from flask import jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.get("/falta_de_promessa")
def falta_de_promessa():
    awnser = function.awnser()
    return awnser


@app.get("/promessa_nao_atende")
def promessa_não_atende():
    lack = function.lack()
    return lack

@app.get("/promessa_a_vencer")
def Promessa_a_vencer():
    win = function.win()
    return win
@app.get("/normal")
def normal():
    normal = function.normal()
    return normal
@app.get("/promessa_Vencida")
def promessa_vencida():
    expired = function.expired()
    return expired

@app.get("/sent_mail")
def sent_email():
    
    My_Address =''
    Passoword =''
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

