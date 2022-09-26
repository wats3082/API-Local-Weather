# WEATHER APP CONNECTING TO 3RD PARTY API
import datetime
import tkinter
import customtkinter
import requests  # import requests to use
from PIL import Image, ImageTk

city = 'Los Angeles'
new = "Conditions loading..."


def getWeather(city):
    # API CONNECTION is our way to communicate with server
    weatherKey = '60d0bd9d21da6aa23ae5d4ec2bfb15e9'  # need to have unique api key from each website in JSON
    url = 'https://api.openweathermap.org/data/2.5/weather?'  # q={city name}&appid={API key}
    params = {'APPID': weatherKey, 'q': city, 'units': 'imperial'}
    response = requests.get(url, params=params)
    weather = response.json()
    print("loading...")
    return ResponseWeather(weather)


"""def getMap(city):
    # API CONNECTION is our way to communicate with server
    weatherKey = '60d0bd9d21da6aa23ae5d4ec2bfb15e9'  # need to have unique api key from each website in JSON
    url = 'http://maps.openweathermap.org/maps/2.0/weather/PA0/2/3/3?'  # q={city name}&appid={API key}
    params = {'APPID': weatherKey, 'q': city, 'units': 'imperial'}
    response = requests.get(url, params=params)
    weather = response.json()
    print("loading map...")"""


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
        main = weather['weather'][0]['main']
        country = weather['sys']['country']


        time = datetime.datetime.now()

        finalOutput = str(name) + ",  " + country + "\nSummary: " + main + "\n" + str(
            temp) + " degrees\n" + str(
            hum) + "% humidity\n" + str(lat) + " latitude\n" + str(lon) + " longitude\n" + str(
            pressure) + " kPa atm pressure\n" + str(wind) + \
                      " mph wind speed\n" + "\n" + str(time)
    except:
        finalOutput = "There was a problem with your search \n" \
                      "check spelling and try again."

    return finalOutput


customtkinter.set_appearance_mode("Dark")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("dark-blue")  # Themes: "blue" (standard), "green", "dark-blue"


class App(customtkinter.CTk):
    WIDTH = 900
    HEIGHT = 600

    def __init__(self):
        super().__init__()

        self.title("RW Weather")
        self.geometry(f"{App.WIDTH}x{App.HEIGHT}")
        # self.minsize(App.WIDTH, App.HEIGHT)

        self.protocol("WM_DELETE_WINDOW", self.on_closing)  # call .on_closing() when app gets closed

        # ============ create two frames ============

        # configure grid layout (2x1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.frame_left = customtkinter.CTkFrame(master=self,
                                                 width=180,
                                                 corner_radius=0)
        self.frame_left.grid(row=0, column=0, sticky="nswe")

        self.frame_right = customtkinter.CTkFrame(master=self)
        self.frame_right.grid(row=0, column=1, sticky="nswe", padx=20, pady=20)

        # ============ frame_left ============

        # configure grid layout (1x11)
        self.frame_left.grid_rowconfigure(0, minsize=10)  # empty row with minsize as spacing
        self.frame_left.grid_rowconfigure(6, weight=1)  # empty row as spacing
        self.frame_left.grid_rowconfigure(8, minsize=20)  # empty row with minsize as spacing
        self.frame_left.grid_rowconfigure(11, minsize=10)  # empty row with minsize as spacing

        self.label_1 = customtkinter.CTkLabel(master=self.frame_left,
                                              text="Weather App",
                                              text_font=("Roboto Medium", 16))  # font name and size in px
        self.label_1.grid(row=1, column=0, pady=30, padx=10)

        self.button_1 = customtkinter.CTkButton(master=self.frame_left,
                                                text="24 hour forecast",
                                                fg_color=("green"),  # <- custom tuple-color
                                                command=self.button_event24,
                                                text_font=("Roboto Medium", 12))
        self.button_1.grid(row=2, column=0, pady=30, padx=20, )

        self.button_2 = customtkinter.CTkButton(master=self.frame_left,
                                                text="Weekly forecast",
                                                fg_color=("green"),  # <- custom tuple-color
                                                command=self.button_eventweek,
                                                text_font=("Roboto Medium", 12))
        self.button_2.grid(row=3, column=0, pady=30, padx=20)
        self.button_3 = customtkinter.CTkButton(master=self.frame_left,
                                                text="Monthly forecast",
                                                fg_color="green",  # <- custom tuple-color
                                                command=self.button_eventmonth,
                                                text_font=("Roboto Medium", 12))
        self.button_3.grid(row=4, column=0, pady=30, padx=20)
        self.button_4 = customtkinter.CTkButton(master=self.frame_left,
                                                text="Hourly",
                                                fg_color="green",  # <- custom tuple-color
                                                command=self.button_eventhourly,
                                                text_font=("Roboto Medium", 12))
        self.button_4.grid(row=5, column=0, pady=30, padx=20)

        self.switch_2 = customtkinter.CTkSwitch(master=self.frame_left,
                                                text="Dark Mode",
                                                command=self.change_mode,
                                                text_font=("Roboto Medium", 12))
        self.switch_2.grid(row=10, column=0, pady=10, padx=20, sticky="w")

        # ============ frame_right ============

        # configure grid layout (3x7)
        self.frame_right.rowconfigure((0, 1, 2, 3), weight=1)
        self.frame_right.rowconfigure(7, weight=5)
        self.frame_right.columnconfigure((0, 1), weight=1)
        self.frame_right.columnconfigure(2, weight=1)

        self.frame_info = customtkinter.CTkFrame(master=self.frame_right)
        self.frame_info.grid(row=0, column=0, columnspan=2, rowspan=4, pady=10, padx=20, sticky="nsew")

        # ============ frame_info ============

        # configure grid layout (1x1)
        self.frame_info.rowconfigure(0, weight=1)
        self.frame_info.columnconfigure(0, weight=1)

        # ============ frame_right ============

        self.radio_var = tkinter.IntVar(value=0)

        self.label_radio_group = customtkinter.CTkLabel(master=self.frame_right,
                                                        text="Choose a city",
                                                        text_font=("Roboto Medium", 16))
        self.label_radio_group.grid(row=0, column=2, columnspan=1, pady=10, padx=10, sticky="")

        self.radio_button_1 = customtkinter.CTkComboBox(master=self.frame_right,
                                                        variable=self.radio_var,
                                                        command=self.button_event,

                                                        values=["Los Angeles", "Chicago", "Miami",
                                                                "Seattle", "Istanbul", "London",
                                                                "Moscow", "Tokyo",
                                                                "Cairo", "Nairobi", "Seoul"],
                                                        text_font=("Roboto Medium", 12)
                                                        )

        self.radio_button_1.grid(row=1, column=2, pady=10, padx=10, sticky="n")
        self.label_radio_group_1 = customtkinter.CTkLabel(master=self.frame_right, text="Made using Python\n"
                                                                                        "Openweather, Tkinter\n"
                                                                                        "Ver 2.1 \n",


                                                          text_font=("Roboto Medium", 12),
                                                          text_color='green')
        self.label_radio_group_1.grid(row=2, column=2, pady=10, padx=10, sticky="")

        # -----------------------------------------------------------------------------------
        self.label_display = customtkinter.CTkLabel(master=self.frame_info,
                                                    text=new,
                                                    height=400,
                                                    width=400,
                                                    fg_color=("white", "black"),  # <- custom tuple-color
                                                    justify=tkinter.CENTER,
                                                    text_font=("Roboto Medium", 15))
        self.label_display.grid(column=0, row=3, sticky="w", padx=15, pady=15),

        self.entry = customtkinter.CTkEntry(master=self.frame_right,
                                            width=120,
                                            height=60,
                                            placeholder_text="Search a city's current weather conditions",
                                            fg_color='black',
                                            text_font=("Roboto Medium", 12))
        self.entry.grid(row=6, column=0, columnspan=2, pady=20, padx=20, sticky="we")

        self.button_5 = customtkinter.CTkButton(master=self.frame_right,
                                                text="Submit",
                                                # command=lambda: getWeather(userCity.get()))
                                                command=self.submit_button_event,
                                                text_font=("Roboto Medium", 12))
        self.button_5.grid(row=6, column=2, columnspan=1, pady=20, padx=20, sticky="we")

        # set default values
        self.radio_button_1.set("Los Angeles")
        self.label_display.set_text(getWeather('Los Angeles'))
        self.switch_2.select()

    def submit_button_event(self):
        global city
        city = self.entry.get()

        print(city)
        self.label_display.set_text(getWeather(city))

    def button_event24(self):
        #self.label_display.set_text(getWeather(city))
        print("open new window")

    def button_eventweek(self):
        #self.label_display.set_text(getWeatherweek(city))
        print("open new window")

    def button_eventmonth(self):
        #self.label_display.set_text(getWeather(city))
        print("open new window")

    def button_eventhourly(self):
        #self.label_display.set_text(getWeather(city))
        print("open new window")


    def button_event(self, event):
        self.label_display.set_text(getWeather(event))

    # print(self.radio_button_1.grab_current())

    def change_mode(self):
        if self.switch_2.get() == 1:
            customtkinter.set_appearance_mode("dark")
        else:
            customtkinter.set_appearance_mode("light")

    def on_closing(self, event=0):
        self.destroy()

    def start(self):
        self.mainloop()


if __name__ == "__main__":
    app = App()
    app.start()
