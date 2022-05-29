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
    if len(currentDay) < 2:
        currentDay = f"0{currentDay}"

    currentHour = currentTime.hour
    if len(currentHour) < 2:
        currentHour = f"0{currentHour}"

    currentMinute = currentTime.minute
    if len(currentMinute) < 2:
        currentMinute = f"0{currentMinute}"

    metarFormatTime = f"{currentDay}{currentHour}{currentMinute}Z"

    infoForShowMetarPage = {
        "metarText": metarResponse.text,
        "timeSearched": metarFormatTime,
        "icaoCode": anIcaoCode.strip().upper()
    }

    # return f"<h1>You searched for {anIcaoCode}</h1><br>Response: {metarResponse.text}"
    return render_template('showMetar.html', info=infoForShowMetarPage)
