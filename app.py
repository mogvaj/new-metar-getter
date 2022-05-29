from flask import Flask, request, render_template
import requests
import json

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/getMetar/<anIcaoCode>")
def getMetar(anIcaoCode: str):
    print (f"Starting getMetar() with an argument of {anIcaoCode}")
    
    return f"<h1>You searched for {anIcaoCode}</h1>"