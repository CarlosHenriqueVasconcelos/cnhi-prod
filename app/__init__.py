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

@app.get("/Falta_de_Promessa")
def falta_de_promessa():
    awnser = function.awnser()
    return awnser


@app.get("/Promessa_não_Atende")
def promessa_não_atende():
    lack = function.lack()
    return lack

@app.get("/Promessa_a_Vencer")
def Promessa_a_vencer():
    win = function.win()
    return win
@app.get("/Normal")
def normal():
    normal = function.normal()
    return normal
@app.get("/Promessa_Vencida")
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

