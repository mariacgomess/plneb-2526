from flask import Flask, render_template, request
import json

app= Flask(__name__)

f_db=open("dicionario_medico.json","r")
db=json.load(f_db)

@app.get("/")
def hello_world():
    return render_template("home.html")

@app.get("/conceitos")
def lista_conceitos():
    termos = sorted(db.keys())
    return render_template("conceitos.html", conceitos=termos)

@app.get("/api/")
def conceitos_api():
    return db


app.run(host="localhost", port=5002, debug=True)