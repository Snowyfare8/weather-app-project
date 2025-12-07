# Weather App
# API data imports
from weatherapi import city, hourly_data, current_temp, current_humidity, current_is_day, current_winddirection, current_windspeed, current_apptemp, current_rain, current_precipitation, current_snowfall, current_showers, current_cloud_cover, current_pressure_msl, current_surfpressure, current_weather_code, current_dust

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
import datetime as dt
import ttkbootstrap as tkbs

# GUI - rework needed
class MasterFrame(ctk.CTkScrollableFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs, label_text = "Python Weather Application")

        # def refresh(self):
        # self.display_frame.destroy()
        # self.display_frame = tk.Frame(self)
        # self.display_frame.grid(row = 2, column = 0, columnspan = 3, sticky = "nsew")

class SummaryFrame(ctk.CTkFrame):
    def __init__(self, MasterFrame, **kwargs):
        super().__init__(MasterFrame, **kwargs)

        day_or_no = "🌞" if current_is_day == 1.0 else "🌙"
        curtemp_text = f"{int(current_temp)}{'°C'}"
        curhumidity_text = f"{int(current_humidity)}{' %'}"
        curwinddir_text = f"{int(current_winddirection)}{' Deg'}"
        curwindspeed_text = f"{int(current_windspeed)}{' m/s'}"
        curprecip_text = f"{int(current_precipitation)}{' mm'}"
        curpressuresl_text = f"{int(current_pressure_msl)}{' hPa'}"
        curpressuresurf_text = f"{int(current_surfpressure)}{' hPa'}"
        curapptemp_text = f"{'Feels like '}{int(current_apptemp)}{'°C'}"
        curcloudcover_text = f"{int(current_cloud_cover)}{' %'}"

        self.curweather = ctk.CTkLabel(self, text = "Current weather")
        self.current_temperature = ctk.CTkLabel(self, text = day_or_no + curtemp_text, font = ("Normal", 25, "normal"))
        self.humidity_text = ctk.CTkLabel(self, text  = "Humidity")
        self.current_humidity = ctk.CTkLabel(self, text = curhumidity_text)
        self.winddirection_text = ctk.CTkLabel(self, text  = "Wind Direction")
        self.current_winddirection = ctk.CTkLabel(self, text = curwinddir_text)
        self.windspeed_text = ctk.CTkLabel(self, text  = "Wind Speed")
        self.current_windspeed = ctk.CTkLabel(self, text = curwindspeed_text)
        self.precip_text = ctk.CTkLabel(self, text = "Precipitation")
        self.current_precip = ctk.CTkLabel(self, text = curprecip_text)
        self.pressuresl_text = ctk.CTkLabel(self, text = "Sea Level Pressure")
        self.current_pressuresl = ctk.CTkLabel(self, text = curpressuresl_text)
        self.pressuresurf_text = ctk.CTkLabel(self, text = "Surface Pressure")
        self.current_pressuresurf = ctk.CTkLabel(self, text = curpressuresurf_text)
        self.current_apptemp = ctk.CTkLabel(self, text = curapptemp_text)
        self.cloudcover_text = ctk.CTkLabel(self, text = "Cloud Cover")
        self.current_cloudcover = ctk.CTkLabel(self, text = curcloudcover_text)

        self.curweather.grid(row = 0, column = 0, padx = 10, pady = 5)
        self.current_temperature.grid(row = 1, column = 0, padx = 0, pady = 10)
        self.humidity_text.grid(row = 2, column = 1, padx = 10, pady = 0, sticky = "s")
        self.current_humidity.grid(row = 3, column = 1, padx = 10, pady = 2)  
        self.winddirection_text.grid(row = 0, column = 2, padx = 10, pady = 0, sticky = "s")
        self.current_winddirection.grid(row = 1, column = 2, padx = 10, pady = 2)
        self.windspeed_text.grid(row = 2, column = 2, padx = 10, pady = 0, sticky = "s")
        self.current_windspeed.grid(row = 3, column = 2, padx = 10, pady = 2)
        self.precip_text.grid(row = 2, column = 4, padx = 10, pady = 0, sticky = "s")
        self.current_precip.grid(row = 3, column = 4, padx = 10, pady = 2)
        self.pressuresl_text.grid(row = 2, column = 5, padx = 10, pady = 0, sticky = "s")
        self.current_pressuresl.grid(row = 3, column = 5, padx = 10, pady = 2)
        self.pressuresurf_text.grid(row = 0, column = 5, padx = 10, pady = 0, sticky = "s")
        self.current_pressuresurf.grid(row = 1, column = 5, padx = 10, pady = 2)
        self.current_apptemp.grid(row = 3, column = 0, padx = 10, pady = 2)
        self.cloudcover_text.grid(row = 0, column = 1, padx = 10, pady = 0, sticky = "s")
        self.current_cloudcover.grid(row = 1, column = 1, padx = 10, pady = 2)

class GraphFrame(ctk.CTkFrame):
    def __init__(self, MasterFrame, **kwargs):
        super().__init__(MasterFrame, **kwargs)

        def temp_weather_graph():
            fig = Figure(figsize = (10, 5), facecolor ="#7A7A7A")

            plot1 = fig.add_subplot(111)

            plot1.plot(hourly_data["date"], hourly_data["temperature_2m"], label = "Temperature (°C)")

            canvas = FigureCanvasTkAgg(fig, master = GraphFrame)  
            canvas.draw()
            canvas.get_tk_widget().grid(row = 2, column = 2, pady = 5, sticky = "w")

            toolbar = NavigationToolbar2Tk(canvas, GraphFrame, pack_toolbar = False)
            toolbar.update()
            canvas.get_tk_widget().grid(row = 2, column = 2, pady = 5, sticky = "w")

            plt.xlabel("By hours")
            plt.ylabel("Temperature (°C)")
            plt.title("Temperature 2m")  
            
        def wind_speed_weather_graph():
            fig = Figure(figsize = (10, 5), facecolor ="#7A7A7A")

            plot1 = fig.add_subplot(111)

            plot1.plot(hourly_data["date"], hourly_data["wind_speed_180m"], label = "Wind Speed (m/s)")

            canvas = FigureCanvasTkAgg(fig, master = GraphFrame)  
            canvas.draw()
            canvas.get_tk_widget().grid(row = 2, column = 2, pady = 5, sticky = "w")

            toolbar = NavigationToolbar2Tk(canvas, GraphFrame, pack_toolbar = False)
            toolbar.update()
            canvas.get_tk_widget().grid(row = 2, column = 2, pady = 5, sticky = "w")

            plt.xlabel("By hours")
            plt.ylabel("Wind Speed (m/s)")
            plt.title("Wind Speed 180m")

        def wind_direction_weather_graph():

            fig = Figure(figsize = (10, 5), facecolor ="#7A7A7A")

            plot1 = fig.add_subplot(111)

            plot1.plot(hourly_data["date"], hourly_data["wind_direction_180m"], label = "Direction (°)")

            canvas = FigureCanvasTkAgg(fig, master = GraphFrame)  
            canvas.draw()
            canvas.get_tk_widget().grid(row = 2, column = 2, pady = 5, sticky = "w")

            toolbar = NavigationToolbar2Tk(canvas, GraphFrame, pack_toolbar = False)
            toolbar.update()
            canvas.get_tk_widget().grid(row = 2, column = 3, pady = 5, sticky = "w")

            plt.xlabel("By hours")
            plt.ylabel("Wind Direction (°)")
            plt.title("Wind Direction 180m")

        def uv_weather_graph():
            fig = Figure(figsize = (10, 5), facecolor ="#7A7A7A")

            plot1 = fig.add_subplot(111)

            plot1.plot(hourly_data["date"], hourly_data["uv_index"], label = "UV Index")

            canvas = FigureCanvasTkAgg(fig, master = GraphFrame)  
            canvas.draw()
            canvas.get_tk_widget().grid(row = 2, column = 2, pady = 5, sticky = "w")

            toolbar = NavigationToolbar2Tk(canvas, GraphFrame, pack_toolbar = False)
            toolbar.update()
            canvas.get_tk_widget().grid(row = 2, column = 2, pady = 5, sticky = "w")

            plt.xlabel("By days")
            plt.ylabel("UV Index")
            plt.title("UV Index Today")

        def humidity_weather_graph():
            fig = Figure(figsize = (10, 5), facecolor ="#7A7A7A")

            plot1 = fig.add_subplot(111)

            plot1.plot(hourly_data["date"], hourly_data["relative_humidity_2m"], label ="Humidity (%)")

            canvas = FigureCanvasTkAgg(fig, master = GraphFrame)  
            canvas.draw()
            canvas.get_tk_widget().grid(row = 2, column = 2, pady = 5, sticky = "w")

            toolbar = NavigationToolbar2Tk(canvas, GraphFrame, pack_toolbar = False)
            toolbar.update()
            canvas.get_tk_widget().grid(row = 2, column = 2, pady = 5, sticky = "w")
    
            plt.xlabel("By hours")
            plt.ylabel("Relative Humidity (%)")
            plt.title("Relative Humidity 2m")  

        self.temp_button = ctk.CTkButton(self, text = "Temperature", border_color = "#FFFFFF", command = lambda:[temp_weather_graph(self)])
        self.windspeed_button = ctk.CTkButton(self, text = "Wind Speed", border_color = "#FFFFFF", command = lambda:[wind_speed_weather_graph(self)])
        self.winddirection_button = ctk.CTkButton(self, text = "Wind Direction", border_color = "#FFFFFF", command = lambda:[wind_direction_weather_graph(self)])
        self.uv_button = ctk.CTkButton(self, text = "UV Index", border_color = "#FFFFFF", command = lambda:[uv_weather_graph(self)])
        self.humidity_button = ctk.CTkButton(self, text = "Humidity", border_color = "#FFFFFF", command = lambda:[humidity_weather_graph(self)])

        self.temp_button.grid(row = 0, column = 0, padx = 10, pady = 20, sticky = "nsew")
        self.windspeed_button.grid(row = 0, column = 1, padx = 10, pady = 20, sticky = "nsew")
        self.winddirection_button.grid(row = 0, column = 2, padx = 10, pady = 20, sticky = "nsew")
        self.uv_button.grid(row = 0, column = 3, padx = 10, pady = 20, sticky = "nsew")
        self.humidity_button.grid(row = 0, column = 4, padx = 10, pady = 20, sticky = "nsew")
        
class DetailsFrame(ctk.CTkFrame):
    def __init__(self, MasterFrame, **kwargs):
        super().__init__(MasterFrame, **kwargs)

        self.detailed_temp = ctk.CTkLabel(self, text = "Temperature")
        self.detailed_apptemp = ctk.CTkLabel(self, text = "Feels like")
        self.detailed_humidity = ctk.CTkLabel(self, text = "Humidity")

        self.detailed_temp.grid(row = 0, column = 0, padx = 10, pady = 5)
        self.detailed_apptemp.grid(row = 0, column = 1, padx = 10, pady = 5)
        self.detailed_humidity.grid(row = 0, column = 2, padx = 10, pady = 5 )


class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.grid_rowconfigure(0, weight = 1)
        self.grid_columnconfigure(0, weight = 1)

        self.master_frame = MasterFrame(master = self, height = 1200, width = 1200, corner_radius = 0, fg_color = "transparent")
        self.master_frame.grid(row = 0, column = 0, sticky = "nsew")

        self.city_label = ctk.CTkLabel(self.master_frame, text = city, font = ("Normal", 22, "bold"))
        self.city_label.grid(row = 0, column = 0, padx = 10, pady = 20, sticky = "w")

        self.display_frame = SummaryFrame(self.master_frame)
        self.display_frame.grid(row = 1, column = 0, padx = 20, pady = 10, sticky = "w")

        self.graph_text = ctk.CTkLabel(self.master_frame, text = "Hourly Weather", font = ("Normal", 20, "italic"))
        self.graph_text.grid(row = 2, column = 0, padx = 10, pady = 10, sticky = "sw")

        self.button_frame = GraphFrame(self.master_frame)
        self.button_frame.grid(row = 3, column = 0, padx = 20, pady = 20, sticky = "sw")

        self.details_text = ctk.CTkLabel(self.master_frame, text = "Weather Details", font = ("Normal", 20, "italic"))
        self.details_text.grid(row = 4, column = 0, padx = 10, pady = 10, sticky = "sw")

        self.details_frame = DetailsFrame(self.master_frame)
        self.details_frame.grid(row = 5, column = 0, padx = 20, pady = 10, sticky = "sw")

        
app = App()

app.mainloop()
