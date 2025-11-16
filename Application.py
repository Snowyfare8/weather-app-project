#Application Prototype
from API import city, daily_data, hourly_data
import numpy as np
import matplotlib as mpl
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
from tkinter import *

# Weather Graphs
def uv_weather_graph():
    fig = Figure(figsize = (10, 5), dpi = 100)

    plt.plot(daily_data["date"], daily_data["uv_index_max"], label="UV Index")
    
    canvas = FigureCanvasTkAgg(fig, master = window)  
    canvas.draw()
    
    canvas.get_tk_widget().pack()
    
    toolbar = NavigationToolbar2Tk(canvas, window)
    toolbar.update()

    canvas.get_tk_widget().pack()

    plt.xlabel("By days")
    plt.ylabel("UV Index")
    plt.title("UV Index Today")
    plt.legend()
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

def temp_weather_graph():
    fig = Figure(figsize = (10, 5), dpi = 100)

    plt.plot(hourly_data["date"], hourly_data["temperature_2m"], label="Temperature (°C)")

    canvas = FigureCanvasTkAgg(fig, master = window)  
    canvas.draw()
    
    canvas.get_tk_widget().pack()

    toolbar = NavigationToolbar2Tk(canvas, window)
    toolbar.update()

    canvas.get_tk_widget().pack()

    plt.xlabel("By hours")
    plt.ylabel("Temperature (°C)")
    plt.title("Temperature 2m")
    plt.legend()
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

def wind_speed_weather_graph():
    fig = Figure(figsize = (10, 5), dpi = 100)

    plt.plot(hourly_data["date"], hourly_data["wind_speed_180m"], label="Wind Speed (m/s)")

    canvas = FigureCanvasTkAgg(fig, master = window)  
    canvas.draw()
  
    canvas.get_tk_widget().pack()

    toolbar = NavigationToolbar2Tk(canvas, window)
    toolbar.update()

    canvas.get_tk_widget().pack()

    plt.xlabel("By hours")
    plt.ylabel("Wind Speed (m/s)")
    plt.title("Wind Speed 180m")    
    plt.legend()
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

def wind_direction_weather_graph():
    fig = Figure(figsize = (10, 5), dpi = 100)

    plt.plot(hourly_data["date"], hourly_data["wind_direction_180m"], label="Direction (°)")

    canvas = FigureCanvasTkAgg(fig, master = window)  
    canvas.draw()

    canvas.get_tk_widget().pack()

    toolbar = NavigationToolbar2Tk(canvas, window)
    toolbar.update()

    canvas.get_tk_widget().pack()

    plt.xlabel("By hours")
    plt.ylabel("Wind Direction (°)")
    plt.title("Wind Direction 180m")
    plt.legend()
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()


def humidity_weather_graph():
    fig = Figure(figsize = (10  , 5), dpi = 100)

    plt.plot(hourly_data["date"], hourly_data["relative_humidity_2m"], label="Humidity (%)")

    canvas = FigureCanvasTkAgg(fig, master = window)  
    canvas.draw()
  
    canvas.get_tk_widget().pack()

    toolbar = NavigationToolbar2Tk(canvas, window)
    toolbar.update()

    canvas.get_tk_widget().pack()
    
    plt.xlabel("By hours")
    plt.ylabel("Relative Humidity (%)")
    plt.title("Relative Humidity 2m")   
    plt.legend()
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

# GUI
window = Tk()
window.title('Python Weather Application')

window.geometry('900x600')
menu = Menu(window)
window.config(menu=menu)
timemenu = Menu(menu)
menu.add_cascade(label='By Time', menu=timemenu)
timemenu.add_command(label='Current')
timemenu.add_command(label='Hourly')
timemenu.add_command(label='Weekly')
menu.add_command(label='Settings')
menu.add_command(label='Exit', command=window.quit)

city_label = Label(window, text='City: ' + city)
currentweather_label = Label(window, text ='Current Weather in ' + city)

temp_label = Label(window, text ='Temperature')
temp_display = Button(window, text = "Temperature Graph", command = temp_weather_graph)

wind_label = Label(window, text='Wind Speed & Direction')
windspeed_display = Button(window, text = "Wind Speed Graph", command = wind_speed_weather_graph)
winddirection_display = Button(window, text = "Wind Direction Graph", command = wind_direction_weather_graph)

uv_label = Label(window, text ='UV Index')
uv_display = Button(window, text = "UV Index Graph", command = uv_weather_graph)

humidity_label = Label(window, text ='Humidity')
humidity_display = Button(window, text = "Humidity Graph", command = humidity_weather_graph)

city_label.pack()
currentweather_label.pack()

temp_label.pack()
temp_display.pack()

wind_label.pack()
windspeed_display.pack()
winddirection_display.pack()

uv_label.pack()
uv_display.pack()

humidity_label.pack()
humidity_display.pack()


window.mainloop()
