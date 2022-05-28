from flask import Flask
import requests
import json

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')