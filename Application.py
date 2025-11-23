#Application Prototype
# API data imports
from API import city, hourly_data
# Graphing imports
import numpy as np
import matplotlib as mpl
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
# GUI imports
import tkinter as tk
import customtkinter as ctk
from customtkinter import *

# Weather Graphs - gui rework needed
def temp_weather_graph():
    fig = Figure(figsize = (10, 5), dpi = 100)

    plot1 = fig.add_subplot(111)

    plot1.plot(hourly_data["date"], hourly_data["temperature_2m"], label="Temperature (°C)")

    canvas = FigureCanvasTkAgg(fig, master = window)  
    canvas.draw()
    canvas.get_tk_widget().grid(row=7, column=0, columnspan=5)

    toolbar = NavigationToolbar2Tk(canvas, window, pack_toolbar=False)
    toolbar.update()
    canvas.get_tk_widget().grid(row=8, column=0, columnspan=5)

    plt.xlabel("By hours")
    plt.ylabel("Temperature (°C)")
    plt.title("Temperature 2m")

def wind_speed_weather_graph():
    fig = Figure(figsize = (10, 5), dpi = 100)

    plot1 = fig.add_subplot(111)

    plot1.plot(hourly_data["date"], hourly_data["wind_speed_180m"], label="Wind Speed (m/s)")

    canvas = FigureCanvasTkAgg(fig, master = window)  
    canvas.draw()
    canvas.get_tk_widget().grid(row=7, column=0, columnspan=5)

    toolbar = NavigationToolbar2Tk(canvas, window, pack_toolbar=False)
    toolbar.update()
    canvas.get_tk_widget().grid(row=8, column=0, columnspan=5)

    plt.xlabel("By hours")
    plt.ylabel("Wind Speed (m/s)")
    plt.title("Wind Speed 180m")    

def wind_direction_weather_graph():

    fig = Figure(figsize = (10, 5), dpi = 100)

    plot1 = fig.add_subplot(111)

    plot1.plot(hourly_data["date"], hourly_data["wind_direction_180m"], label="Direction (°)")

    canvas = FigureCanvasTkAgg(fig, master = window)  
    canvas.draw()
    canvas.get_tk_widget().grid(row=7, column=0, columnspan=5)

    toolbar = NavigationToolbar2Tk(canvas, window, pack_toolbar=False)
    toolbar.update()
    canvas.get_tk_widget().grid(row=8, column=0, columnspan=5)

    plt.xlabel("By hours")
    plt.ylabel("Wind Direction (°)")
    plt.title("Wind Direction 180m")

def uv_weather_graph():
    fig = Figure(figsize = (10, 5), dpi = 100)

    plot1 = fig.add_subplot(111)

    plot1.plot(hourly_data["date"], hourly_data["uv_index"], label="UV Index")

    canvas = FigureCanvasTkAgg(fig, master = window)  
    canvas.draw()
    canvas.get_tk_widget().grid(row=7, column=0, columnspan=5)

    toolbar = NavigationToolbar2Tk(canvas, window, pack_toolbar=False)
    toolbar.update()
    canvas.get_tk_widget().grid(row=8, column=0, columnspan=5)

    plt.xlabel("By days")
    plt.ylabel("UV Index")
    plt.title("UV Index Today")

def humidity_weather_graph():
    fig = Figure(figsize = (10  , 5), dpi = 100)

    plot1 = fig.add_subplot(111)

    plot1.plot(hourly_data["date"], hourly_data["relative_humidity_2m"], label="Humidity (%)")

    canvas = FigureCanvasTkAgg(fig, master = window)  
    canvas.draw()
    canvas.get_tk_widget().grid(row=7, column=0, columnspan=5)

    toolbar = NavigationToolbar2Tk(canvas, window, pack_toolbar=False)
    toolbar.update()
    canvas.get_tk_widget().grid(row=8, column=0, columnspan=5)
    
    plt.xlabel("By hours")
    plt.ylabel("Relative Humidity (%)")
    plt.title("Relative Humidity 2m")   

# GUI - rework needed
window = ctk.CTk()  
window.title('Python Weather Application')
window.geometry('1200x800')


city_label = ctk.CTkLabel(window, text='Your City: ' + city, font = ("Courier New", 22, "bold"))
currentweather_label = ctk.CTkLabel(window, text ='Current Weather in ' + city, font = ("Courier New", 18))

temp_button = ctk.CTkButton(window, text = "Temperature Graph", command = temp_weather_graph)

windspeed_button = ctk.CTkButton(window, text = "Wind Speed Graph", command = wind_speed_weather_graph)
winddirection_button = ctk.CTkButton(window, text = "Wind Direction Graph", command = wind_direction_weather_graph)

uv_button = ctk.CTkButton(window, text = "UV Index Graph", command = uv_weather_graph)

humidity_button = ctk.CTkButton(window, text = "Humidity Graph", command = humidity_weather_graph)

city_label.grid(row = 0, column = 0, sticky = W, padx = 10, pady = 10)
currentweather_label.grid(row = 3, column = 0, sticky = W, padx = 10, pady = 10)

temp_button.grid(row = 6, column = 0, sticky = W, padx = 10, pady = 10)

windspeed_button.grid(row = 6, column = 1, padx = 10, pady = 10)

winddirection_button.grid(row = 6, column = 2, padx = 10, pady = 10)

uv_button.grid(row = 6, column = 3, padx = 10, pady = 10)

humidity_button.grid(row = 6, column = 4, padx = 10, pady = 10)

window.mainloop()
