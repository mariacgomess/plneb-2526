from flask import Flask, render_template, request
import json

app= Flask(__name__)

f_db=open("dicionario_medico.json","r")
db=json.load(f_db)

@app.get("/")
def hello_world():
    return render_template("conceitos.html")
@app.get("/api/")
def conceitos_api():
    return db

app.run(host="localhost", port=4002, debug=True)