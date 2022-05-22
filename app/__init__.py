from flask import Flask
from app.functions.function import read_archive
from app.functions.function import choose_table
from app.functions.function import emails
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email import encoders
import smtplib
from pprint import pprint
import json

app = Flask(__name__)

@app.get("/all")
def all_archives():
    result = read_archive()
    return {"resultData": result}


@app.get("/all/table")
def table():
    resultado = choose_table()
    result = resultado.to_json(orient="index")
    parsed = json.loads(result)
    json1 = json.dumps(parsed,sort_keys=True)
    print(json1)
  
    #   result = [dict(zip(("LEAD TIME DAYS", "ORIGIN", "SUPPLIER","CNH PART NUMBER","DESCRIPTION","ISSUE DATE","PO NUMBER","REQUESTED DATE","PROM SHIP DATE","REQ QTY","PROM QTY","QTY TYPE","REMARKS","PLANTS"), row)) for i, row in resultado.items()]

    return {"tabela escolhida": json1}
   
@app.get("/all/table/email")
def email():
    My_Address ='carlos@fmloliveira.com'
    Passoword ='solrac22'
    text, email = emails()
    email2 = [email]
    print(My_Address)
    print(Passoword)

    msg = MIMEText(text, 'plain')
    msg['From']=My_Address
    msg['To']= '.join([‘cnhi@fmloliveira.com’])'
    msg['Subject']="This is TEST"
    raw = msg.as_string()

    s = smtplib.SMTP(host='smtp-relay.gmail.com', port= 25)
    SMTP.starttls()
    s.login(My_Address, Passoword)

    smtp.sendmail(My_Address, email2, raw)
    smtp.quit()
    return {"TESTE": enviou}