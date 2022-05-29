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
    metarFormatTime = f"{currentTime.day}{currentTime.hour}{currentTime.minute}Z"

    infoForShowMetarPage = {
        "metarText": metarResponse.text,
        "timeSearched": metarFormatTime,
        "icaoCode": anIcaoCode.strip().upper()
    }

    # return f"<h1>You searched for {anIcaoCode}</h1><br>Response: {metarResponse.text}"
    return render_template('showMetar.html', info=infoForShowMetarPage)
