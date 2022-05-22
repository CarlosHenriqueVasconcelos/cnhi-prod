from flask import Flask
from http import HTTPStatus
from app.functions import function
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email import encoders
import smtplib
from pprint import pprint
import json
from flask import jsonify

app = Flask(__name__)


@app.get("/all_table")
def read_all_table():
    result = function.choose_table()
    parsed = function.normalize_invoices(result)

    response = jsonify(parsed)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response
   
# @app.get("/all/table/email")
# def email():
#     My_Address ='carlos@fmloliveira.com'
#     Passoword ='solrac22'
#     text, email = emails()
#     email2 = [email]
#     print(My_Address)
#     print(Passoword)

#     msg = MIMEText(text, 'plain')
#     msg['From']=My_Address
#     msg['To']= '.join([‘cnhi@fmloliveira.com’])'
#     msg['Subject']="This is TEST"
#     raw = msg.as_string()

#     s = smtplib.SMTP(host='smtp-relay.gmail.com', port= 25)
#     SMTP.starttls()
#     s.login(My_Address, Passoword)

#     smtp.sendmail(My_Address, email2, raw)
#     smtp.quit()
#     return {"TESTE": enviou}