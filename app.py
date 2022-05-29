from flask import Flask, request, render_template
import requests
from datetime import datetime, timezone

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/getMetar/<anIcaoCode>")
def getMetar(anIcaoCode: str):
    metarResponse = requests.get("https://beta.aviationweather.gov/cgi-bin/data/metar.php?ids=" + anIcaoCode)
    
    currentTime = datetime.now(timezone.utc)
    
    currentDay = currentTime.day
    if currentDay < 10:
        currentDay = f"0{currentDay}"

    currentHour = currentTime.hour
    if currentHour < 10:
        currentHour = f"0{currentHour}"

    currentMinute = currentTime.minute
    if currentMinute < 10:
        currentMinute = f"0{currentMinute}"

    metarFormatTime = f"{currentDay}{currentHour}{currentMinute}Z"

    infoForShowMetarPage = {
        "metarText": metarResponse.text,
        "timeSearched": metarFormatTime,
        "icaoCode": anIcaoCode.strip().upper()
    }

    return render_template('showMetar.html', info=infoForShowMetarPage)
