# WEATHER APP CONNECTING TO 3RD PARTY API
from tkinter import *
import requests  # import requests to use

root = Tk()
root.title("OPEN WEATHER FORECAST")
root.geometry("500x300")

def ResponseWeather(weather):
    try:
        name= weather['name']
        desc = weather['weather'][0]['description']
        temp = weather['main']['temp']
        finalOutput = str(name) + " currently has " + str(desc) + " and " + str(temp) + " degrees."
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
    #print(ResponseWeather(weather))


label1 = Label(root, text="Type in city name to fetch weather.")
label1.grid(row=0, column=0)
button1 = Button(root, text="Get Weather", command=lambda: getWeather(userCity.get()))
button1.grid(row=2, column=0, padx=10, pady=20, columnspan=2)
userCity = Entry(root, width=20)
userCity.grid(row=1, column=0, padx=10, pady=20, columnspan=2)
label2 = Label(root, bd=10)
label2.grid(row=3, column=0)

root.mainloop()
