# Weather App
# API data imports
from weatherapi import *
from airqualityapi import *

# Imaging imports
from PIL import Image

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
import time as t

ctk.set_appearance_mode("system")
ctk.set_default_color_theme("blue")

# GUI
class MasterFrame(ctk.CTkScrollableFrame):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

class SummaryFrame(ctk.CTkFrame):
    def __init__(self, MasterFrame, **kwargs):
        super().__init__(MasterFrame, **kwargs)

        def euaqi_grade_func(current_euroaqi):
            if current_euroaqi >= 100:
                return "Extremely Poor"
            elif current_euroaqi >= 80:
                return "Very Poor"
            elif current_euroaqi >= 60:
                return "Poor"
            elif current_euroaqi >= 40:
                return "Moderate"
            elif current_euroaqi >= 20:
                return "Fair"
            else:
                return "Good"

        daylight_var = "🌞" if current_is_day == 1.0 else "🌙"
        precipitation_var = "🌧️Medium to Heavy Rain" if current_precipitation > 0.0 else "☁️Little to No Rain"
        curtemp_text = f"{int(current_temp)}{'°C'}"
        curhumidity_text = f"{int(current_humidity)}{' %'}"
        curwinddir_text = f"{int(current_winddirection)}{' Deg'}"
        curwindspeed_text = f"{int(current_windspeed)}{' m/s'}"
        curprecip_text = f"{int(current_precipitation)}{' mm'}"
        curpressuresl_text = f"{int(current_pressure_msl)}{' hPa'}"
        curpressuresurf_text = f"{int(current_surfpressure)}{' hPa'}"
        curapptemp_text = f"{'Feels like '}{int(current_apptemp)}{'°C'}"
        curcloudcover_text = f"{int(current_cloud_cover)}{' %'}"
        curdust_text = f"{int(current_dust)}{' μg/m^3'}"
        curaqi_text = f"{int(current_euroaqi)}{' EU AQI'}"

        def summary_display(self):       

            self.curweather = ctk.CTkLabel(self, text = "Current weather")
            self.current_temperature = ctk.CTkLabel(self, text = daylight_var + curtemp_text, font = ("Normal", 25, "normal"))

            self.precipitation_status = ctk.CTkLabel(self, text = precipitation_var)

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

            self.dust_text = ctk.CTkLabel(self, text = "Dustiness")
            self.current_dust = ctk.CTkLabel(self, text = curdust_text)

            self.aqi_text = ctk.CTkLabel(self, text = "Air Quality")
            self.current_aqi = ctk.CTkLabel(self, text = curaqi_text)

            self.aqi_grade = ctk.CTkLabel(self, text = euaqi_grade_func(current_euroaqi))

            self.curweather.grid(row = 0, column = 0, padx = 15, pady = 5)
            self.current_temperature.grid(row = 1, column = 0, padx = 15, pady = 10)

            self.precipitation_status.grid(row = 2, column = 0, padx = 15, pady = 10)

            self.humidity_text.grid(row = 2, column = 1, padx = 15, pady = 0, sticky = "s")
            self.current_humidity.grid(row = 3, column = 1, padx = 15, pady = 2)  

            self.winddirection_text.grid(row = 0, column = 2, padx = 15, pady = 0, sticky = "s")
            self.current_winddirection.grid(row = 1, column = 2, padx = 15, pady = 2)

            self.windspeed_text.grid(row = 2, column = 2, padx = 15, pady = 0, sticky = "s")
            self.current_windspeed.grid(row = 3, column = 2, padx = 15, pady = 2)

            self.precip_text.grid(row = 0, column = 4, padx = 15, pady = 0, sticky = "s")
            self.current_precip.grid(row = 1, column = 4, padx = 15, pady = 2)

            self.pressuresl_text.grid(row = 2, column = 5, padx = 15, pady = 0, sticky = "s")
            self.current_pressuresl.grid(row = 3, column = 5, padx = 15, pady = 2)

            self.pressuresurf_text.grid(row = 0, column = 5, padx = 15, pady = 0, sticky = "s")
            self.current_pressuresurf.grid(row = 1, column = 5, padx = 15, pady = 2)

            self.current_apptemp.grid(row = 3, column = 0, padx = 15, pady = 2)
            self.cloudcover_text.grid(row = 0, column = 1, padx = 15, pady = 0, sticky = "s")

            self.current_cloudcover.grid(row = 1, column = 1, padx = 15, pady = 2)
            self.dust_text.grid(row = 0, column = 6, padx = 15, pady = 0, sticky = "s")

            self.current_dust.grid(row = 1, column = 6, padx = 15, pady = 2)
            self.aqi_text.grid(row = 2, column = 6, padx = 15, pady = 0, sticky = "s")

            self.current_aqi.grid(row = 3, column = 6, padx = 15, pady = 2)
            self.aqi_grade.grid(row = 4, column = 6, padx = 15, pady = 2)

        euaqi_grade_func(current_euroaqi)
        summary_display(self)

class HourlyGraphFrame(ctk.CTkFrame):
    def __init__(self, MasterFrame, **kwargs):
        super().__init__(MasterFrame, **kwargs)

        def temp_hourly_graph():
            fig = Figure(figsize = (10, 5), facecolor ="#FFFFFF", dpi = 100, edgecolor = "#FFFFFF" )

            plot1 = fig.add_subplot(111)

            plot1.plot(hourly_data["date"], hourly_data["temperature_2m"], label = "Temperature (°C)")

            canvas = FigureCanvasTkAgg(fig, master = self)  
            canvas.draw()
            canvas.get_tk_widget().grid(row = 1, column = 0, columnspan = 6, padx = 5, pady = 5, sticky = "w")

            toolbar = NavigationToolbar2Tk(canvas, self, pack_toolbar = False)
            toolbar.update()
            canvas.get_tk_widget().grid(row = 1, column = 0, columnspan = 6, padx = 5, pady = 5, sticky = "w")

            plot1.set_xlabel("By hours (x-axis)")
            plot1.set_ylabel("Temperature (°C) (y-axis)")
            plot1.set_title("Temperature 2m")

        def wind_speed_hourly_graph():
            fig = Figure(figsize = (10, 5), facecolor ="#FFFFFF", dpi = 100, edgecolor = "#FFFFFF" )

            plot1 = fig.add_subplot(111)

            plot1.plot(hourly_data["date"], hourly_data["wind_speed_180m"], label = "Wind Speed (m/s)")

            canvas = FigureCanvasTkAgg(fig, master = self)  
            canvas.draw()
            canvas.get_tk_widget().grid(row = 1, column = 0, columnspan = 6, padx = 5, pady = 5, sticky = "w")

            toolbar = NavigationToolbar2Tk(canvas, self, pack_toolbar = False)
            toolbar.update()
            canvas.get_tk_widget().grid(row = 1, column = 0, columnspan = 6, padx = 5, pady = 5, sticky = "w")

            plot1.set_xlabel("By hours (x-axis)")
            plot1.set_ylabel("Wind Speed (m/s) (y-axis)")
            plot1.set_title("Wind Speed 180m")

        def wind_direction_hourly_graph():
            fig = Figure(figsize = (10, 5), facecolor ="#FFFFFF", dpi = 100, edgecolor = "#FFFFFF" )

            plot1 = fig.add_subplot(111)

            plot1.plot(hourly_data["date"], hourly_data["wind_direction_180m"], label = "Direction (°)")

            canvas = FigureCanvasTkAgg(fig, master = self)  
            canvas.draw()
            canvas.get_tk_widget().grid(row = 1, column = 0, columnspan = 6, padx = 5, pady = 5, sticky = "w")

            toolbar = NavigationToolbar2Tk(canvas, self, pack_toolbar = False)
            toolbar.update()
            canvas.get_tk_widget().grid(row = 1, column = 0, columnspan = 6, padx = 5, pady = 5, sticky = "w")

            plot1.set_xlabel("By hours (x-axis)")
            plot1.set_ylabel("Wind Direction (°) (y-axis)")
            plot1.set_title("Wind Direction 180m")

        def uv_hourly_graph():
            fig = Figure(figsize = (10, 5), facecolor ="#FFFFFF", dpi = 100, edgecolor = "#FFFFFF" )

            plot1 = fig.add_subplot(111)

            plot1.plot(hourly_data["date"], hourly_data["uv_index"], label = "UV Index")

            canvas = FigureCanvasTkAgg(fig, master = self)  
            canvas.draw()
            canvas.get_tk_widget().grid(row = 1, column = 0, columnspan = 6, padx = 5, pady = 5, sticky = "w")

            toolbar = NavigationToolbar2Tk(canvas, self, pack_toolbar = False)
            toolbar.update()
            canvas.get_tk_widget().grid(row = 1, column = 0, columnspan = 6, padx = 5, pady = 5, sticky = "w")

            plot1.set_xlabel("By days (x-axis)")
            plot1.set_ylabel("UV Index (y-axis)")
            plot1.set_title("UV Index Today")

        def humidity_hourly_graph():
            fig = Figure(figsize = (10, 5), facecolor ="#FFFFFF", dpi = 100, edgecolor = "#FFFFFF" )

            plot1 = fig.add_subplot(111)

            plot1.plot(hourly_data["date"], hourly_data["relative_humidity_2m"], label = "Humidity (%)")

            canvas = FigureCanvasTkAgg(fig, master = self)  
            canvas.draw()
            canvas.get_tk_widget().grid(row = 1, column = 0, columnspan = 6, padx = 5, pady = 5, sticky = "w")

            toolbar = NavigationToolbar2Tk(canvas, self, pack_toolbar = False)
            toolbar.update()
            canvas.get_tk_widget().grid(row = 1, column = 0, columnspan = 6, padx = 5, pady = 5, sticky = "w")
    
            plot1.set_xlabel("By hours (x-axis)")
            plot1.set_ylabel("Relative Humidity (%) (y-axis)")
            plot1.set_title("Relative Humidity 2m")  

        def precipitation_hourly_graph():
            fig = Figure(figsize = (10, 5), facecolor ="#FFFFFF", dpi = 100, edgecolor = "#FFFFFF" )

            plot1 = fig.add_subplot(111)

            plot1.plot(hourly_data["date"], hourly_data["precipitation"], label = "Precipitation (mm)")

            canvas = FigureCanvasTkAgg(fig, master = self)  
            canvas.draw()
            canvas.get_tk_widget().grid(row = 1, column = 0, columnspan = 6, padx = 5, pady = 5, sticky = "w")

            toolbar = NavigationToolbar2Tk(canvas, self, pack_toolbar = False)
            toolbar.update()
            canvas.get_tk_widget().grid(row = 1, column = 0, columnspan = 6, padx = 5, pady = 5, sticky = "w")
    
            plot1.set_xlabel("By hours (x-axis)")
            plot1.set_ylabel("Precipitation (mm)(y-axis)")
            plot1.set_title("Precipitation (Rain, snow, and/or hail)")  

        self.temp_hourly_button = ctk.CTkButton(self, text = "Temperature", border_color = "#FFFFFF", command = temp_hourly_graph)
        self.windspeed_hourly_button = ctk.CTkButton(self, text = "Wind Speed", border_color = "#FFFFFF", command = wind_speed_hourly_graph)
        self.winddirection_hourly_button = ctk.CTkButton(self, text = "Wind Direction", border_color = "#FFFFFF", command = wind_direction_hourly_graph)
        self.uv_hourly_button = ctk.CTkButton(self, text = "UV Index", border_color = "#FFFFFF", command = uv_hourly_graph)
        self.humidity_hourly_button = ctk.CTkButton(self, text = "Humidity", border_color = "#FFFFFF", command = humidity_hourly_graph)
        self.precipitation_hourly_button = ctk.CTkButton(self, text = "Precipitation", border_color = "#FFFFFF", command = precipitation_hourly_graph)

        self.temp_hourly_button.configure(height = 5, width = 15)
        self.windspeed_hourly_button.configure(height = 5, width = 15)
        self.winddirection_hourly_button.configure(height = 5, width = 15)
        self.uv_hourly_button.configure(height = 5, width = 15) 
        self.humidity_hourly_button.configure(height = 5, width = 15)
        self.precipitation_hourly_button.configure(height = 5, width = 15)

        self.temp_hourly_button.grid(row = 0, column = 0, padx = 10, pady = 20, sticky = "nsew")
        self.windspeed_hourly_button.grid(row = 0, column = 1, padx = 10, pady = 20, sticky = "nsew")
        self.winddirection_hourly_button.grid(row = 0, column = 2, padx = 10, pady = 20, sticky = "nsew")
        self.uv_hourly_button.grid(row = 0, column = 3, padx = 10, pady = 20, sticky = "nsew")
        self.humidity_hourly_button.grid(row = 0, column = 4, padx = 10, pady = 20, sticky = "nsew")
        self.precipitation_hourly_button.grid (row = 0, column = 5, padx = 10, pady = 20, sticky = "nsew") 

        temp_hourly_graph()

class AirQualityFrame(ctk.CTkFrame):
    def __init__(self, MasterFrame, **kwargs):
        super().__init__(MasterFrame, **kwargs)

        pm10_display = f"{int(current_pm10)}{' μg/m^3'}"
        pm2_5_display = f"{int(current_pm2_5)}{' μg/m^3'}"
        co_display = f"{int(current_co)}{' μg/m^3'}"
        no2_display = f"{int(current_no2)}{' μg/m^3'}"
        so2_display = f"{int(current_so2)}{' μg/m^3'}"
        o3_display = f"{int(current_o3)}{' μg/m^3'}"

        def air_quality_display(self):
            self.pm10_text = ctk.CTkLabel(self, text = "Particulate Matter 10")
            self.current_pm10 = ctk.CTkLabel(self, text = pm10_display)

            self.pm2_5_text = ctk.CTkLabel(self, text = "Particulate Matter 2.5")
            self.current_pm25 = ctk.CTkLabel(self, text = pm2_5_display)

            self.co_text = ctk.CTkLabel(self, text = "Carbon Monoxide")
            self.current_co = ctk.CTkLabel(self, text = co_display)

            self.no2_text = ctk.CTkLabel(self, text = "Nitrogen Dioxide") 
            self.current_no2 = ctk.CTkLabel(self, text = no2_display)

            self.so2_text = ctk.CTkLabel(self, text = "Sulfur Dioxide")
            self.current_so2 = ctk.CTkLabel(self, text = so2_display)

            self.o3_text = ctk.CTkLabel(self, text = "Ozone")
            self.current_o3 = ctk.CTkLabel(self, text = o3_display)

            self.pm10_text.grid(row = 0, column = 0, padx = 10, pady = 5)
            self.current_pm10.grid(row = 1, column = 0, padx = 10, pady = 5)

            self.pm2_5_text.grid(row = 0, column = 1, padx = 10, pady = 5)
            self.current_pm25.grid(row = 1, column = 1, padx = 10, pady = 5)

            self.co_text.grid(row = 0, column = 2, padx = 10, pady = 5)
            self.current_co.grid(row = 1, column = 2, padx = 10, pady = 5)

            self.no2_text.grid(row = 0, column = 3, padx = 10, pady = 5)
            self.current_no2.grid(row = 1, column = 3, padx = 10, pady = 5)

            self.so2_text.grid(row = 0, column = 4, padx = 10, pady = 5)
            self.current_so2.grid(row = 1, column = 4, padx = 10, pady = 5)

            self.o3_text.grid(row = 0, column = 5, padx = 10, pady = 5)
            self.current_o3.grid(row = 1, column = 5, padx = 10, pady = 5)
       
        air_quality_display(self)

class MinutelyGraphFrame(ctk.CTkFrame):
    def __init__(self, MasterFrame, **kwargs):
        super().__init__(MasterFrame, **kwargs)

        def temp_minutely_graph():
            fig = Figure(figsize = (10, 5), facecolor ="#FFFFFF", dpi = 100, edgecolor = "#FFFFFF" )

            plot1 = fig.add_subplot(111)

            plot1.plot(minutely_15_data["date"], minutely_15_data["temperature_2m"], label = "Temperature (°C)")

            canvas = FigureCanvasTkAgg(fig, master = self)  
            canvas.draw()
            canvas.get_tk_widget().grid(row = 1, column = 0, columnspan = 6, padx = 5, pady = 5, sticky = "w")

            toolbar = NavigationToolbar2Tk(canvas, self, pack_toolbar = False)
            toolbar.update()
            canvas.get_tk_widget().grid(row = 1, column = 0, columnspan = 6, padx = 5, pady = 5, sticky = "w")

            plot1.set_xlabel("By minutes (x-axis)")
            plot1.set_ylabel("Temperature (°C) (y-axis)")
            plot1.set_title("Temperature 2m")       

        def humidity_minutely_graph():
            fig = Figure(figsize = (10, 5), facecolor ="#FFFFFF", dpi = 100, edgecolor = "#FFFFFF" )

            plot1 = fig.add_subplot(111)

            plot1.plot(minutely_15_data["date"], minutely_15_data["relative_humidity_2m"], label = "Humidity (%)")

            canvas = FigureCanvasTkAgg(fig, master = self)  
            canvas.draw()
            canvas.get_tk_widget().grid(row = 1, column = 0, columnspan = 6, padx = 5, pady = 5, sticky = "w")

            toolbar = NavigationToolbar2Tk(canvas, self, pack_toolbar = False)
            toolbar.update()
            canvas.get_tk_widget().grid(row = 1, column = 0, columnspan = 6, padx = 5, pady = 5, sticky = "w")

            plot1.set_xlabel("By minutes (x-axis)")
            plot1.set_ylabel("Humidity (%) (y-axis)")
            plot1.set_title("Relative Humidity 2m")     

        def apparent_temp_minutely_graph():
            fig = Figure(figsize = (10, 5), facecolor ="#FFFFFF", dpi = 100, edgecolor = "#FFFFFF" )

            plot1 = fig.add_subplot(111)

            plot1.plot(minutely_15_data["date"], minutely_15_data["apparent_temperature"], label = "Apparent Temperature (°C)")

            canvas = FigureCanvasTkAgg(fig, master = self)  
            canvas.draw()
            canvas.get_tk_widget().grid(row = 1, column = 0, columnspan = 6, padx = 5, pady = 5, sticky = "w")

            toolbar = NavigationToolbar2Tk(canvas, self, pack_toolbar = False)
            toolbar.update()
            canvas.get_tk_widget().grid(row = 1, column = 0, columnspan = 6, padx = 5, pady = 5, sticky = "w")

            plot1.set_xlabel("By minutes (x-axis)")
            plot1.set_ylabel("Apparent Temperature (°C) (y-axis)")
            plot1.set_title("Apparent Temperature")    

        def wind_speed_minutely_graph():
            fig = Figure(figsize = (10, 5), facecolor ="#FFFFFF", dpi = 100, edgecolor = "#FFFFFF" )

            plot1 = fig.add_subplot(111)

            plot1.plot(minutely_15_data["date"], minutely_15_data["wind_speed_80m"], label = "Wind Speed (m/s)")

            canvas = FigureCanvasTkAgg(fig, master = self)  
            canvas.draw()
            canvas.get_tk_widget().grid(row = 1, column = 0, columnspan = 6, padx = 5, pady = 5, sticky = "w")

            toolbar = NavigationToolbar2Tk(canvas, self, pack_toolbar = False)
            toolbar.update()
            canvas.get_tk_widget().grid(row = 1, column = 0, columnspan = 6, padx = 5, pady = 5, sticky = "w")

            plot1.set_xlabel("By minutes (x-axis)")
            plot1.set_ylabel("Wind Speed (m/s) (y-axis)")
            plot1.set_title("Wind Speed 80m")    

        def wind_direction_minutely_graph():
            fig = Figure(figsize = (10, 5), facecolor ="#FFFFFF", dpi = 100, edgecolor = "#FFFFFF" )

            plot1 = fig.add_subplot(111)

            plot1.plot(minutely_15_data["date"], minutely_15_data["relative_humidity_2m"], label = "Wind Direction (°) ")

            canvas = FigureCanvasTkAgg(fig, master = self)  
            canvas.draw()
            canvas.get_tk_widget().grid(row = 1, column = 0, columnspan = 6, padx = 5, pady = 5, sticky = "w")

            toolbar = NavigationToolbar2Tk(canvas, self, pack_toolbar = False)
            toolbar.update()
            canvas.get_tk_widget().grid(row = 1, column = 0, columnspan = 6, padx = 5, pady = 5, sticky = "w")

            plot1.set_xlabel("By minutes (x-axis)")
            plot1.set_ylabel("Wind Direction (°) (y-axis)")
            plot1.set_title("Wind Direction 80m")   

        def precipitation_minutely_graph():
            fig = Figure(figsize = (10, 5), facecolor ="#FFFFFF", dpi = 100, edgecolor = "#FFFFFF" )

            plot1 = fig.add_subplot(111)

            plot1.plot(minutely_15_data["date"], minutely_15_data["precipitation"], label = "Precipitation (mm)")

            canvas = FigureCanvasTkAgg(fig, master = self)  
            canvas.draw()
            canvas.get_tk_widget().grid(row = 1, column = 0, columnspan = 6, padx = 5, pady = 5, sticky = "w")

            toolbar = NavigationToolbar2Tk(canvas, self, pack_toolbar = False)
            toolbar.update()
            canvas.get_tk_widget().grid(row = 1, column = 0, columnspan = 6, padx = 5, pady = 5, sticky = "w")

            plot1.set_xlabel("By minutes (x-axis)")
            plot1.set_ylabel("Precipitation (mm) (y-axis)")
            plot1.set_title("Precipitation (Rain, snow, and/or hail)")

        self.temp_minutely_button = ctk.CTkButton(self, text = "Temperature", border_color = "#FFFFFF", command = temp_minutely_graph )
        self.humidity_minutely_button = ctk.CTkButton(self, text = "Humidity", border_color = "#FFFFFF", command = humidity_minutely_graph )
        self.apparent_temp_minutely_button = ctk.CTkButton(self, text = "Apparent Temperature", border_color = "#FFFFFF", command = apparent_temp_minutely_graph )
        self.wind_speed_minutely_button = ctk.CTkButton(self, text = "Wind Speed", border_color = "#FFFFFF", command = wind_speed_minutely_graph )
        self.wind_direction_minutely_button = ctk.CTkButton(self, text = "Wind Direction", border_color = "#FFFFFF", command = wind_direction_minutely_graph )
        self.precipitation_minutely_button = ctk.CTkButton(self, text = "Precipitation", border_color = "#FFFFFF", command = precipitation_minutely_graph )

        self.temp_minutely_button.configure(height = 5, width = 15)
        self.humidity_minutely_button.configure(height = 5, width = 15)
        self.apparent_temp_minutely_button.configure(height = 5, width = 15)
        self.wind_speed_minutely_button.configure(height = 5, width = 15) 
        self.wind_direction_minutely_button.configure(height = 5, width = 15)
        self.precipitation_minutely_button.configure(height = 5, width = 15)

        self.temp_minutely_button.grid(row = 0, column = 0, padx = 10, pady = 20, sticky = "nsew")
        self.humidity_minutely_button.grid(row = 0, column = 1, padx = 10, pady = 20, sticky = "nsew")
        self.apparent_temp_minutely_button.grid(row = 0, column = 2, padx = 10, pady = 20, sticky = "nsew")
        self.wind_speed_minutely_button.grid(row = 0, column = 3, padx = 10, pady = 20, sticky = "nsew")
        self.wind_direction_minutely_button.grid(row = 0, column = 4, padx = 10, pady = 20, sticky = "nsew")
        self.precipitation_minutely_button.grid(row = 0, column = 5, padx = 10, pady = 20, sticky = "nsew")

        temp_minutely_graph()

class OptionsSidebarFrame(ctk.CTkFrame):
    def __init__(self, MasterFrame, **kwargs):
        super().__init__(MasterFrame, **kwargs)

        self.settings_label = ctk.CTkLabel(self, text = "GUI Settings", font = ("Normal", 12, "bold"))

        self.settings_label.grid(row = 0, column = 0, padx = 20, pady = 10)

        self.set_appearance_mode_label = ctk.CTkLabel(self, text = "UI Color Mode")
        self.set_appearance_mode_label.grid(row = 1, column = 0, padx = 20, pady = (10, 2))

        self.set_ui_scaling_label = ctk.CTkLabel(self, text = "UI Rescaling")
        self.set_ui_scaling_label.grid(row = 3, column = 0, padx = 20, pady = (10, 2))

        self.misc_label = ctk.CTkLabel(self, text = "Miscellaneous", font = ("Normal", 12, "bold"))
        self.misc_label.grid(row = 5, column = 0, padx = 20, pady = (20, 5))

        self.information_label = ctk.CTkLabel(self, text = "Information about the Program", font = ("Normal", 12, "bold"))
        self.information_textbox = ctk.CTkTextbox(self, state = "normal")

        self.information_textbox.insert("0.0", "This program's GUI was created using CustomTkinter, a modernized fork of python library Tkinter and uses Open-Meteo for the weather data, Open-Meteo is an open-source meteorological forecasting API.")

        self.information_label.grid(row = 6, column = 0, padx = 20, pady = (10, 2))
        self.information_textbox.grid(row = 7, column = 0, padx = 20, pady = (3, 10))

class App(ctk.CTk):
    width = 1180
    height = 800

    def __init__(self):
        super().__init__()

        self.title("Python Weather App")
        self.geometry(f"{self.width}x{self.height}")
        self.resizable(False, False)

        self.grid_rowconfigure((0, 1, 2, 3, 4, 5), weight = 1)
        self.grid_columnconfigure((0, 1, 2), weight = 1)

        self.master_frame = MasterFrame(master = self, height = self.height, width = self.width, corner_radius = 0, fg_color = "transparent")
        self.master_frame.grid(row = 0, column = 0, sticky = "nsew")

        self.city_label = ctk.CTkLabel(self.master_frame, text = city, font = ("Normal", 22, "bold"), fg_color = "transparent")
        self.city_label.grid(row = 0, column = 0, padx = 20, pady = (20, 10), sticky = "nw")

        self.display_frame = SummaryFrame(self.master_frame, border_color = "dark_color")
        self.display_frame.grid(row = 1, column = 0, padx = 10, sticky = "nw")

        self.hourly_graph_label = ctk.CTkLabel(self.master_frame, text = "Hourly Weather Graphs", font = ("Normal", 20, "bold"), fg_color = "transparent")
        self.hourly_graph_label.grid(row = 2, column = 0, padx = 20, pady = (40, 10), sticky = "nw")

        self.hourly_graph_frame = HourlyGraphFrame(self.master_frame, border_color = "dark_color")
        self.hourly_graph_frame.grid(row = 3, column = 0, padx = 20, sticky = "nw") 

        self.minutely_graph_label = ctk.CTkLabel(self.master_frame, text = "Minutely Weather Graphs", font = ("Normal", 20, "bold"), fg_color = "transparent")
        self.minutely_graph_label.grid(row = 4, column = 0, padx = 20, pady = (40, 10), sticky = "nw")

        self.minutely_graph_frame = MinutelyGraphFrame(self.master_frame, border_color  = "dark_color")
        self.minutely_graph_frame.grid(row = 5, column = 0, padx = 20, pady = (0, 20), sticky = "nw")

        self.airquality_label = ctk.CTkLabel(self.master_frame, text = "Air Quality Details", font = ("Normal", 20, "bold"), fg_color = "transparent")
        self.airquality_label.grid(row = 6, column = 0, padx = 20, pady = (40, 10), sticky = "nw")

        self.airquality_frame = AirQualityFrame(self.master_frame, border_color = "dark_color")
        self.airquality_frame.grid(row = 7, column = 0, padx = 20, pady = (0, 200) sticky = "nw")

        self.options_frame = OptionsSidebarFrame(self.master_frame, border_color = "dark_color")
        self.options_frame.grid(row = 0, column = 1, rowspan = 800, padx = (40, 0), pady = 10, sticky = "ns")

        self.set_appearance_mode_menu = ctk.CTkOptionMenu(self.options_frame, values = ["System", "Light", "Dark"], command = self.change_appearance_mode)
        self.set_ui_scaling = ctk.CTkOptionMenu(self.options_frame, values = ["80%", "90%", "100%", "110%", "120%"], command = self.change_ui_scaling)

        self.set_appearance_mode_menu.grid(row = 2, column = 0, padx = 20, pady = (0, 20))
        self.set_ui_scaling.grid(row = 4, column = 0, padx = 20, pady = (0, 20))

        self.set_ui_scaling.set("100%")

    def change_appearance_mode(self, new_appearance_mode: str):
        ctk.set_appearance_mode(new_appearance_mode)
         
    def change_ui_scaling(self, new_ui_scaling: str):
        new_scaling_float = int(new_ui_scaling.replace("%", "")) / 100
        ctk.set_widget_scaling(new_scaling_float)

if __name__ == "__main__":
    app = App()
    app.mainloop()

