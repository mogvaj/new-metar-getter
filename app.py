from flask import Flask, request, render_template
import requests
from datetime import datetime, timezone, timedelta

app = Flask(__name__)

@app.route("/")
@app.route("/index/<anIcaoCode>")
def index(anIcaoCode: str = "KPIH"):
    infoForIndexPage = {
        "icaoCode": anIcaoCode
    }

    return render_template('index.html', info=infoForIndexPage)

@app.route("/getMetar/<anIcaoCode>")
def getMetar(anIcaoCode: str):
    metarResponse = requests.get("https://beta.aviationweather.gov/cgi-bin/data/metar.php?ids=" + anIcaoCode)
    
    metarTimeString = metarResponse.text.split()[1].replace('Z', '')
    metarYear = currentTime.year
    metarMonth = currentTime.month
    metarDay = int(metarTimeString[0:2])
    metarHour = int(metarTimeString[2:4])
    metarMinute = int(metarTimeString[4:])
    metarTime = datetime(metarYear, metarMonth, metarDay, metarHour, metarMinute, 0, 0, timezone.utc)
    metarAge = currentTime - metarTime

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

    airportInfo = requests.get("https://airport-data.com/api/ap_info.json?icao=" + anIcaoCode)
    airportName = airportInfo.name
    airportLocation = airportInfo.location

    infoForShowMetarPage = {
        "airportName": airportName,
        "airportLocation": airportLocation,
        "metarText": metarResponse.text,
        "timeSearched": metarFormatTime,
        "metarAge": int(metarAge.total_seconds() / 60),
        "icaoCode": anIcaoCode.strip().upper()
    }

    return render_template('showMetar.html', info=infoForShowMetarPage)
