import os
import requestes
from flask import Flask, request, jsonify, json

app = Flask(__name__)

@app.route("/primeira/<nome>")
def ok(nome):
    return "Nome: "+nome

@app.route('/segunda/')
def page2():
    return '<h1> Esse foi um teste de api flask. </h1>'

app.run(host="0.0.0.0", port= 2000, debug= False)

#teste feito seguindo o tutorial no youtube no canal do erikson bastos, obg por compartilhar o conhecimento
