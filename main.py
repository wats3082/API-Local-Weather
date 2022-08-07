# WEATHER APP CONNECTING TO 3RD PARTY API
from tkinter import *
import requests  # import requests to use
from flask import Flask
import datetime

from bottle import route, run

app = Flask(__name__)

root = Tk()
root.title("WEATHER FORECAST")
root.geometry("350x500")


def ResponseWeather(weather):
    try:
        name = weather['name']
        desc = weather['weather'][0]['description']
        temp = weather['main']['temp']
        hum = weather['main']['humidity']
        lat = weather['coord']['lat']
        lon = weather['coord']['lon']
        wind = weather['wind']['speed']
        pressure = weather['main']['pressure']
        time = datetime.datetime.now()

        finalOutput = str(name) + " \nConditions as of " + str(time) + " \nCurrently: " + str(desc) + "\n" + str(temp) + " degrees\n" + str(
            hum) + "% humidity\n" + str(lat) + " latitude\n" + str(lon) + " longitude\n" + str(
            pressure) + " kPa atmospheric pressure\n" + str(wind) + " m/s wind speed\n"
    except:
        finalOutput = "There was a problem with your search."
    return finalOutput


def getWeather(city):
    # API CONNECTION is our way to communicate with server
    weatherKey = '60d0bd9d21da6aa23ae5d4ec2bfb15e9'  # need to have unique api key from each website in JSON
    url = 'https://api.openweathermap.org/data/2.5/weather?'  # q={city name}&appid={API key}
    params = {'APPID': weatherKey, 'q': city, 'units': 'imperial'}
    response = requests.get(url, params=params)
    weather = response.json()
    label2['text'] = ResponseWeather(weather)
    # print(ResponseWeather(weather))


label1 = Label(root, text="Type in city name to fetch weather.")
label1.grid(row=0, column=0)
button1 = Button(root, text="Get Weather", command=lambda: getWeather(userCity.get()))
button1.grid(row=2, column=0, padx=10, pady=20, columnspan=2)
userCity = Entry(root, width=20)
userCity.grid(row=1, column=0, padx=10, pady=20, columnspan=2)
label2 = Label(root, bd=10)
label2.grid(row=3, column=0)

root.mainloop()
