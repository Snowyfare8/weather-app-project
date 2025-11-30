# Application Prototype
# API data imports
from API import city, hourly_data, current_temp, current_humidity, current_is_day, current_winddirection, current_windspeed, current_apptemp

# Graphing imports
import numpy as np
import matplotlib as mpl
from matplotlib.figure import *
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)

# GUI imports
import tkinter as tk
import customtkinter as ctk
from customtkinter import *
import seaborn as sb


# GUI - rework needed
class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title('Python Weather Application')
        self.geometry('1200x800')

        #self.grid_columnconfigure(0, weight = 1)
        #for r in range(6):
        #self.grid_rowconfigure(r, weight = 0)

        self.button_frame = ctk.CTkFrame(self)
        self.button_frame.grid(row = 5, column = 0, padx = 10, pady = 20)

        self.display_frame = ctk.CTkFrame(self)
        self.display_frame.grid(row = 1, column = 0, padx = 10, pady = 10, sticky = "w")

        # Weather Graphs - gui rework needed
        def temp_weather_graph():
            fig = Figure(figsize = (10, 5), facecolor ="#7A7A7A")

            plot1 = fig.add_subplot(111)
    
            plot1.plot(hourly_data["date"], hourly_data["temperature_2m"], label = "Temperature (°C)")

            canvas = FigureCanvasTkAgg(fig, master = self.button_frame)  
            canvas.draw()
            canvas.get_tk_widget().grid(row = 5, column = 3, pady = 5)

            toolbar = NavigationToolbar2Tk(canvas, self.button_frame, pack_toolbar = False)
            toolbar.update()
            canvas.get_tk_widget().grid(row = 5, column = 3, pady = 5)

            plt.xlabel("By hours")
            plt.ylabel("Temperature (°C)")
            plt.title("Temperature 2m")   

        def wind_speed_weather_graph():
            fig = Figure(figsize = (10, 5), facecolor ="#7A7A7A")

            plot1 = fig.add_subplot(111)

            plot1.plot(hourly_data["date"], hourly_data["wind_speed_180m"], label = "Wind Speed (m/s)")

            canvas = FigureCanvasTkAgg(fig, master = self.button_frame)  
            canvas.draw()
            canvas.get_tk_widget().grid(row = 5, column = 3, pady = 5)

            toolbar = NavigationToolbar2Tk(canvas, self.button_frame, pack_toolbar = False)
            toolbar.update()
            canvas.get_tk_widget().grid(row = 5, column = 3, pady = 5)

            plt.xlabel("By hours")
            plt.ylabel("Wind Speed (m/s)")
            plt.title("Wind Speed 180m")  

        def wind_direction_weather_graph():

            fig = Figure(figsize = (10, 5), facecolor ="#7A7A7A")

            plot1 = fig.add_subplot(111)

            plot1.plot(hourly_data["date"], hourly_data["wind_direction_180m"], label = "Direction (°)")

            canvas = FigureCanvasTkAgg(fig, master = self.button_frame)  
            canvas.draw()
            canvas.get_tk_widget().grid(row = 5, column = 3, pady = 5)

            toolbar = NavigationToolbar2Tk(canvas, self.button_frame, pack_toolbar = False)
            toolbar.update()
            canvas.get_tk_widget().grid(row = 5, column = 3, pady = 5)

            plt.xlabel("By hours")
            plt.ylabel("Wind Direction (°)")
            plt.title("Wind Direction 180m")

        def uv_weather_graph():
            fig = Figure(figsize = (10, 5), facecolor ="#7A7A7A")

            plot1 = fig.add_subplot(111)

            plot1.plot(hourly_data["date"], hourly_data["uv_index"], label = "UV Index")

            canvas = FigureCanvasTkAgg(fig, master = self.button_frame)  
            canvas.draw()
            canvas.get_tk_widget().grid(row = 5, column = 3, pady = 5)

            toolbar = NavigationToolbar2Tk(canvas, self.button_frame, pack_toolbar = False)
            toolbar.update()
            canvas.get_tk_widget().grid(row = 5, column = 3, pady = 5)

            plt.xlabel("By days")
            plt.ylabel("UV Index")
            plt.title("UV Index Today")

        def humidity_weather_graph():
            fig = Figure(figsize = (10, 5), facecolor ="#7A7A7A")

            plot1 = fig.add_subplot(111)

            plot1.plot(hourly_data["date"], hourly_data["relative_humidity_2m"], label ="Humidity (%)")

            canvas = FigureCanvasTkAgg(fig, master = self.button_frame)  
            canvas.draw()
            canvas.get_tk_widget().grid(row = 5, column = 3, pady = 5)

            toolbar = NavigationToolbar2Tk(canvas, self.button_frame, pack_toolbar = False)
            toolbar.update()
            canvas.get_tk_widget().grid(row = 5, column = 3, pady = 5)
    
            plt.xlabel("By hours")
            plt.ylabel("Relative Humidity (%)")
            plt.title("Relative Humidity 2m")   

        day_or_no = "🌞" if current_is_day == 1.0 else "🌙"

        curtemp_text = f"{int(current_temp)}{' C'}"
        curhumidity_text = f"{int(current_humidity)}{' %'}"
        curwinddir_text = f"{int(current_winddirection)}{' Deg'}"
        curwindspeed_text = f"{int(current_windspeed)}{' m/s'}"
        curapptemp_text = f"{'Feels like '}{int(current_apptemp)}{' C'}"

        self.curweather = ctk.CTkLabel(self.display_frame, text = "Current weather")
        self.city_label = ctk.CTkLabel(self, text = city, font = ("Helvetica", 22, "bold"))
        self.current_temperature = ctk.CTkLabel(self.display_frame, text = day_or_no + curtemp_text, font = ("Helvetica", 25, "normal"))
        self.humidity_text = ctk.CTkLabel(self.display_frame, text  = "Humidity", font = ("Normal", 9, "normal"))
        self.current_humidity = ctk.CTkLabel(self.display_frame, text = curhumidity_text)
        self.winddirection_text = ctk.CTkLabel(self.display_frame, text  = "Wind Direction", font = ("Normal", 9, "normal"))
        self.current_winddirection = ctk.CTkLabel(self.display_frame, text = curwinddir_text)
        self.windspeed_text = ctk.CTkLabel(self.display_frame, text  = "Wind Speed", font = ("Normal", 9, "normal"))
        self.current_windspeed = ctk.CTkLabel(self.display_frame, text = curwindspeed_text)
        self.current_apptemp = ctk.CTkLabel(self.display_frame, text = curapptemp_text)

        self.curweather.grid(row = 1, column = 0, padx = 10, pady = 5)
        self.city_label.grid(row = 0, column = 0, padx = 10, pady = 5, sticky = "w")
        self.current_temperature.grid(row = 2, column = 0, padx = 0, pady = 10)
        self.current_apptemp.grid(row = 4, column = 0, padx = 10, pady = 5)
        self.humidity_text.grid(row = 3, column = 1, padx = 10, pady = 0 )
        self.current_humidity.grid(row = 4, column = 1, padx = 10, pady = 0)  
        self.windspeed_text.grid(row = 3, column = 2, padx = 10, pady = 0)
        self.current_windspeed.grid(row = 4, column = 2, padx = 10, pady = 0)
        self.winddirection_text.grid(row = 3, column = 3, padx = 10, pady = 0)
        self.current_winddirection.grid(row = 4, column = 3, padx = 10, pady = 0)

        self.temp_button = ctk.CTkButton(self.button_frame, text = "Hourly Temperature", border_color = "#FFFFFF", command = temp_weather_graph)
        self.windspeed_button = ctk.CTkButton(self.button_frame, text = "Hourly Wind Speed", border_color = "#FFFFFF", command = wind_speed_weather_graph)
        self.winddirection_button = ctk.CTkButton(self.button_frame, text = "Hourly Wind Direction", border_color = "#FFFFFF", command = wind_direction_weather_graph)
        self.uv_button = ctk.CTkButton(self.button_frame, text = "Hourly UV Index", border_color = "#FFFFFF", command = uv_weather_graph)
        self.humidity_button = ctk.CTkButton(self.button_frame, text = "Hourly Humidity", border_color = "#FFFFFF", command = humidity_weather_graph)

        self.temp_button.grid(row = 5, column = 0, padx = 10, pady = 20, sticky = "w")
        self.windspeed_button.grid(row = 5, column = 1, padx = 10, pady = 20, sticky = "w")
        self.winddirection_button.grid(row = 5, column = 2, padx = 10, pady = 20, sticky = "w")
        self.uv_button.grid(row = 5, column = 3, padx = 10, pady = 20, sticky = "w")
        self.humidity_button.grid(row = 5, column = 4, padx = 10, pady = 20, sticky = "w")
        
app = App()
app.mainloop()
