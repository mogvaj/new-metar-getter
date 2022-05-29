from flask import Flask, request, render_template
import requests
import json

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/getMetar/<anIcaoCode>")
def getMetar(anIcaoCode: str):
    metarText = requests.get("https://beta.aviationweather.gov/cgi-bin/data/metar.php?ids=" + anIcaoCode)

    return f"<h1>You searched for {anIcaoCode}</h1><br>Response: {metarText}"
