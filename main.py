import requests
from datetime import datetime
import smtplib
import time
#
MY_LAT = 9.0331401 # Your latitude
MY_LONG = 38.750080 # Your longitude
My_email="alyseraby@gmail.com"
Password="wxhivhtpegcpyncw"
#
def iss_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    if MY_LAT - 5 <= iss_latitude <= MY_LAT + 5 and MY_LONG - 5 <= iss_longitude <= MY_LONG + 5:
        return True
def is_night():

    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0 }
    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now().hour

    if time_now>=sunset or time_now<=sunrise:
        return True

while True:
    time.sleep(60)
    if is_night() and iss_overhead():
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(My_email,Password)
            connection.sendmail(from_addr=My_email,
                                to_addrs=My_email,
                                msg="subject: It's Time\n\n Look Up!")


