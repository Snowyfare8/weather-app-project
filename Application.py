#Application Prototype
import openmeteo_requests
import pandas as pd
import requests_cache
from retry_requests import retry
from tkinter import *
import requests

# Geolocator
city = input('Enter city: ')
geo_url = "https://geocoding-api.open-meteo.com/v1/search"
geo_params = {"name": city, "count": 1}
geo_res = requests.get(geo_url, params=geo_params).json()

# API 1
cache_session = requests_cache.CachedSession('.cache', expire_after = 3600)
retry_session = retry(cache_session, retries = 5, backoff_factor = 0.2)
openmeteo = openmeteo_requests.Client(session = retry_session)

# API 2
if "results" in geo_res:
    lat = geo_res["results"][0]["latitude"]
    lon = geo_res["results"][0]["longitude"]

    url = "https://api.open-meteo.com/v1/forecast"
    params = {
        "latitude": lat,
        "longitude": lon,
        "current": ["temperature_2m", "relative_humidity_2m", "wind_speed_10m", "wind_direction_10m"]
        "daily": ["uv_index_max"]
    }
    responses = openmeteo.weather_api(url, params=params)

    response = responses[0]
    current = response.Current()
    current_temp = current.Variables(0).ValuesAsNumpy()
    current_humidity = current.Variables(1).ValuesAsNumpy()
    current_windspeed = current.Variables(2).ValuesAsNumpy()
    current_winddirection = current.Variables(3).ValuesAsNumpy()

    daily_data = {"date": pd.date_range(
        start = pd.to_datetime(daily.Time(), unit = "s", utc = True),
        end = pd.to_datetime(daily.TimeEnd(), unit = "s", utc = True),
        freq = pd.Timedelta(seconds = daily.Interval()),
        inclusive = "left"
    )}

    daily_data["uv_index_max"] = daily_uvindex


# GUI
window = Tk()
window.title('Python Weather Application')

window.geometry('900x600')

city_label = Label(window, text='City: ' + city)

currentweather_label = Label(window, text ='Current Weather in ' + city)

temp_label = Label(window, text ='Temperature')
temp_display = Label(window, text = {"current_temperature_2m"})

wind_label = Label(window, text='Wind Speed & Direction')
windspeed_display = Label(window, text = {"current_wind_speed_10m"})
winddirection_display = Label(window, text = {"current_wind_direction_10m"})

uv_label = Label(window, text ='UV Index')
uv_display = Label(window, text = daily_data["uv_index_max"] )

humidity_label = Label(window, text ='Humidity')
humidity_display = Label(window, text = {"current_relative_humidity_2m"})


city_label.grid(row = 0, column = 1, sticky = W, padx = 2, pady = 2 )
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

