# Weather App
# API data imports
from weatherapi import *
from airqualityapi import *
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

# GUI - rework needed
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

            self.update_idletasks()
            t.sleep(2)

        euaqi_grade_func(current_euroaqi)
        summary_display(self)
    
class GraphFrame(ctk.CTkFrame):
    def __init__(self, MasterFrame, **kwargs):
        super().__init__(MasterFrame, **kwargs)

        def temp_weather_graph():
            fig.clear()
            fig = Figure(figsize = (10, 5), facecolor ="#7A7A7A")

            plot1 = fig.add_subplot(111)

            plot1.plot(hourly_data["date"], hourly_data["temperature_2m"], label = "Temperature (°C)")

            canvas = FigureCanvasTkAgg(fig, master = self)  
            canvas.draw()
            canvas.get_tk_widget().grid(row = 2, column = 0, padx = 5, pady = 5, sticky = "w")

            toolbar = NavigationToolbar2Tk(canvas, self, pack_toolbar = False)
            toolbar.update()
            canvas.get_tk_widget().grid(row = 2, column = 0, padx = 5, pady = 5, sticky = "w")

            plt.xlabel("By hours")
            plt.ylabel("Temperature (°C)")
            plt.title("Temperature 2m")    

        def wind_speed_weather_graph():
            fig.clear()
            fig = Figure(figsize = (10, 5), facecolor ="#7A7A7A")

            plot1 = fig.add_subplot(111)

            plot1.plot(hourly_data["date"], hourly_data["wind_speed_180m"], label = "Wind Speed (m/s)")

            canvas = FigureCanvasTkAgg(fig, master = self)  
            canvas.draw()
            canvas.get_tk_widget().grid(row = 2, column = 0, padx = 5, pady = 5, sticky = "w")

            toolbar = NavigationToolbar2Tk(canvas, self, pack_toolbar = False)
            toolbar.update()
            canvas.get_tk_widget().grid(row = 2, column = 0, padx = 5, pady = 5, sticky = "w")

            plt.xlabel("By hours")
            plt.ylabel("Wind Speed (m/s)")
            plt.title("Wind Speed 180m")

        def wind_direction_weather_graph():
            fig.clear()
            fig = Figure(figsize = (10, 5), facecolor ="#7A7A7A")

            plot1 = fig.add_subplot(111)

            plot1.plot(hourly_data["date"], hourly_data["wind_direction_180m"], label = "Direction (°)")

            canvas = FigureCanvasTkAgg(fig, master = self)  
            canvas.draw()
            canvas.get_tk_widget().grid(row = 2, column = 0, padx = 5, pady = 5, sticky = "w")

            toolbar = NavigationToolbar2Tk(canvas, self, pack_toolbar = False)
            toolbar.update()
            canvas.get_tk_widget().grid(row = 2, column = 0, padx = 5, pady = 5, sticky = "w")

            plt.xlabel("By hours")
            plt.ylabel("Wind Direction (°)")
            plt.title("Wind Direction 180m")

        def uv_weather_graph():
            fig.clear()
            fig = Figure(figsize = (10, 5), facecolor ="#7A7A7A")

            plot1 = fig.add_subplot(111)

            plot1.plot(hourly_data["date"], hourly_data["uv_index"], label = "UV Index")

            canvas = FigureCanvasTkAgg(fig, master = self)  
            canvas.draw()
            canvas.get_tk_widget().grid(row = 2, column = 0, padx = 5, pady = 5, sticky = "w")

            toolbar = NavigationToolbar2Tk(canvas, self, pack_toolbar = False)
            toolbar.update()
            canvas.get_tk_widget().grid(row = 2, column = 0, padx = 5, pady = 5, sticky = "w")

            plt.xlabel("By days")
            plt.ylabel("UV Index")
            plt.title("UV Index Today")

        def humidity_weather_graph():
            fig.clear()
            fig = Figure(figsize = (10, 5), facecolor ="#7A7A7A")

            plot1 = fig.add_subplot(111)

            plot1.plot(hourly_data["date"], hourly_data["relative_humidity_2m"], label ="Humidity (%)")

            canvas = FigureCanvasTkAgg(fig, master = self)  
            canvas.draw()
            canvas.get_tk_widget().grid(row = 2, column = 0, padx = 5, pady = 5, sticky = "w")

            toolbar = NavigationToolbar2Tk(canvas, self, pack_toolbar = False)
            toolbar.update()
            canvas.get_tk_widget().grid(row = 2, column = 0, padx = 5, pady = 5, sticky = "w")
    
            plt.xlabel("By hours")
            plt.ylabel("Relative Humidity (%)")
            plt.title("Relative Humidity 2m")  

        self.temp_button = ctk.CTkButton(self, text = "Temperature", border_color = "#FFFFFF", command = temp_weather_graph)
        self.windspeed_button = ctk.CTkButton(self, text = "Wind Speed", border_color = "#FFFFFF", command = wind_speed_weather_graph)
        self.winddirection_button = ctk.CTkButton(self, text = "Wind Direction", border_color = "#FFFFFF", command = wind_direction_weather_graph)
        self.uv_button = ctk.CTkButton(self, text = "UV Index", border_color = "#FFFFFF", command = uv_weather_graph)
        self.humidity_button = ctk.CTkButton(self, text = "Humidity", border_color = "#FFFFFF", command = humidity_weather_graph)

        self.temp_button.configure(height = 5, width = 15)
        self.windspeed_button.configure(height = 5, width = 15)
        self.winddirection_button.configure(height = 5, width = 15)
        self.uv_button.configure(height = 5, width = 15) 
        self.humidity_button.configure(height = 5, width = 15)

        self.temp_button.grid(row = 0, column = 0, padx = 10, pady = 20, sticky = "nsew")
        self.windspeed_button.grid(row = 0, column = 1, padx = 10, pady = 20, sticky = "nsew")
        self.winddirection_button.grid(row = 0, column = 2, padx = 10, pady = 20, sticky = "nsew")
        self.uv_button.grid(row = 0, column = 3, padx = 10, pady = 20, sticky = "nsew")
        self.humidity_button.grid(row = 0, column = 4, padx = 10, pady = 20, sticky = "nsew")
        
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

            self.update_idletasks()
            t.sleep(2)
       
        air_quality_display(self)

class OptionsSidebarFrame(ctk.CTkFrame):
    def __init__(self, MasterFrame, **kwargs):
        super().__init__(MasterFrame, **kwargs)

        self.settings_label = ctk.CTkLabel(self, text = "GUI Settings")

        self.settings_label.grid(row = 0, column = 0, padx = 20, pady = 10)

        self.set_appearance_mode_label = ctk.CTkLabel(self, text = "UI Color Mode")
        self.set_appearance_mode_label.grid(row = 1, column = 0, padx = 20, pady = (10, 2))

        self.set_ui_scaling_label = ctk.CTkLabel(self, text = "UI Rescaling")
        self.set_ui_scaling_label.grid(row = 3, column = 0, padx = 20, pady = (10, 2))

class App(ctk.CTk):
    width = 910
    height = 800

    def __init__(self):
        super().__init__()

        self.title("Python Weather App")
        self.resizable(True, True)

        self.grid_rowconfigure((0, 1, 2, 3, 4, 5), weight = 1)
        self.grid_columnconfigure((0, 1), weight = 1)

        self.city_label = ctk.CTkLabel(self, text = city, font = ("Normal", 22, "bold"), fg_color = "transparent")
        self.city_label.grid(row = 0, column = 0, padx = 20, pady = (20, 10), sticky = "nw")

        self.display_frame = SummaryFrame(self, border_color = "dark_color")
        self.display_frame.grid(row = 1, column = 0, padx = 10, sticky = "nw")

        self.graph_label = ctk.CTkLabel(self, text = "Hourly Weather", font = ("Normal", 20, "bold"), fg_color = "transparent")
        self.graph_label.grid(row = 2, column = 0, padx = 20, pady = (40, 10), sticky = "nw")

        self.button_frame = GraphFrame(self, border_color = "dark_color")
        self.button_frame.grid(row = 3, column = 0, padx = 20, sticky = "nw") 

        self.airquality_label = ctk.CTkLabel(self, text = "Air Quality Details", font = ("Normal", 20, "bold"), fg_color = "transparent")
        self.airquality_label.grid(row = 4, column = 0, padx = 20, pady = (40, 10), sticky = "nw")

        self.airquality_frame = AirQualityFrame(self, border_color = "dark_color")
        self.airquality_frame.grid(row = 5, column = 0, padx = 20, pady = (0, 200), sticky = "nw")

        self.options_frame = OptionsSidebarFrame(self)
        self.options_frame.grid(row = 0, column = 1, rowspan = 800, padx = 10, pady = 10, sticky = "nse")

        self.set_appearance_mode_menu = ctk.CTkOptionMenu(self.options_frame, values = ["System", "Light", "Dark"], command = self.change_appearance_mode)
        self.set_ui_scaling = ctk.CTkOptionMenu(self.options_frame, values = ["80%", "90%", "100%", "110%", "120%"], command = self.change_ui_scaling)

        self.set_appearance_mode_menu.grid(row = 2, column = 0, padx = 20, pady = (0, 20))
        self.set_ui_scaling.grid(row = 4, column = 0, padx = 20, pady = 0)

        self.set_ui_scaling.set("100%")

    def change_appearance_mode(self, new_appearance_mode: str):
        ctk.set_appearance_mode(new_appearance_mode)
         
    def change_ui_scaling(self, new_ui_scaling: str):
        new_scaling_float = int(new_ui_scaling.replace("%", "")) / 100
        ctk.set_widget_scaling(new_scaling_float)

if __name__ == "__main__":
    app = App()
    app.mainloop()

