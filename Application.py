#Application Prototype
from API import daily_data, hourly_data
import numpy as np
import matplotlib as mpl
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
from tkinter import *


# Weather Graphs
def uv_weather_graph():
    fig = Figure(figsize = (5, 5), dpi = 100)

    x = np.array(daily_data["date"])
    y = np.array(daily_data["uv_index_max"])
    
    canvas = FigureCanvasTkAgg(fig, master = window)  
    canvas.draw()
    
    canvas.get_tk_widget().grid(row = 10, column = 1)
    
    plt.plot(x, y)
    plt.xlabel("By days")
    plt.ylabel("UV Index")

    plt.title("UV Index Today")

def temp_weather_graph():
    fig = Figure(figsize = (5, 5), dpi = 100)

    x = np.array(hourly_data["date"])
    y = np.array(hourly_data["temperature_2m"])

    canvas = FigureCanvasTkAgg(fig, master = window)  
    canvas.draw()
    
    canvas.get_tk_widget().grid(row = 10, column = 1)

    plt.plot(x, y)
    plt.xlabel("By hours")
    plt.ylabel("Temperature (°C)")

    plt.title("Temperature 2m")

def wind_speed_weather_graph():
    fig = Figure(figsize = (5, 5), dpi = 100)

    x = np.array(hourly_data["date"])
    y = np.array(hourly_data["wind_speed_180m"])

    canvas = FigureCanvasTkAgg(fig, master = window)  
    canvas.draw()
  
    canvas.get_tk_widget().grid(row = 10, column = 1)

    plt.plot(x, y)
    plt.xlabel("By hours")
    plt.ylabel("Wind Speed (m/s)")

    plt.title("Wind Speed 180m")    

def wind_direction_weather_graph():
    fig = Figure(figsize = (5, 5), dpi = 100)

    x = np.array(hourly_data["date"])
    y = np.array(hourly_data["wind_direction_180m"])

    canvas = FigureCanvasTkAgg(fig, master = window)  
    canvas.draw()

    canvas.get_tk_widget().grid(row = 10, column = 1)

    plt.plot(x, y)
    plt.xlabel("By hours")
    plt.ylabel("Wind Direction (°)")

    plt.title("Wind Direction 180m")

def humidity_weather_graph():
    fig = Figure(figsize = (5, 5), dpi = 100)

    x = np.array(hourly_data["date"])
    y = np.array(hourly_data["relative_humidity_2m"])

    canvas = FigureCanvasTkAgg(fig, master = window)  
    canvas.draw()
  
    canvas.get_tk_widget().grid(row = 10, column = 1)
    
    plt.plot(x, y)
    plt.xlabel("By hours")
    plt.ylabel("Relative Humidity (%)")

    plt.title("Relative Humidity 2m")   

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
city_entry = Entry(window)(window, width=20, command = city)
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

city_label.grid(row = 0, column = 1, sticky = W, padx = 2, pady = 2 )
city_entry.grid(row = 0, column = 2, sticky = W, padx = 2, pady = 2)
currentweather_label.grid(row = 3, column = 1, sticky = W, padx = 2, pady = 50) 

temp_label.grid(row = 6, column = 1, sticky = W, padx = 2, pady = 2)
temp_display.grid(row = 7, column = 1, sticky = W, padx = 2, pady = 2)

wind_label.grid(row = 6, column = 3, sticky = W, padx = 2, pady = 2)
windspeed_display.grid(row = 7, column = 2, sticky = W, padx = 2, pady =2)
winddirection_display.grid(row = 7, column = 3, sticky = W, padx = 2, pady = 2)

uv_label.grid(row = 6, column = 4, sticky = W, padx = 2, pady = 2)
uv_display.grid(row = 7, column =4, sticky = W, padx = 2, pady = 2)

humidity_label.grid(row = 6, column = 5, sticky = W, padx = 2, pady = 2)
humidity_display.grid(row = 7, column = 5, sticky = W, padx = 2, pady = 2)


window.mainloop()
