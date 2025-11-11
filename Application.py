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
        "hourly": ["temperature_2m","relative_humidity_2m","wind_speed_180m","wind_direction_180m", "uv_index"]
    }
    responses = openmeteo.weather_api(url, params=params)

    response = responses[0]
    hourly = response.Hourly()
    hourly_temp = hourly.Variables(0).ValuesAsNumpy()
    hourly_humidity = hourly.Variables(1).ValuesAsNumpy()
    hourly_windspeed = hourly.Variables(2).ValuesAsNumpy()
    hourly_winddirection = hourly.Variables(3).ValuesAsNumpy()
    hourly_uvindex = hourly.Variables(4).ValuesAsNumpy()

    hourly_data = {"date": pd.date_range(
        start = pd.to_datetime(hourly.Time(), unit = "s", utc = True),
        end = pd.to_datetime(hourly.TimeEnd(), unit = "s", utc = True),
        freq = pd.Timedelta(seconds = hourly.Interval()),
        inclusive = "left"
    )}

    # Assign hourly data to hourly variables
    hourly_data["temperature_2m"] = hourly_temp
    hourly_data["relative_humidity_2m"] = hourly_humidity
    hourly_data["wind_speed_180m"] = hourly_windspeed
    hourly_data["wind_direction_180m"] = hourly_winddirection
    hourly_data["uv_index"] = hourly_uvindex


# GUI
window = Tk()
window.title('Python Weather Application')

window.geometry('900x600')

city_label = Label(window, text='City: ' + city)

currentweather_label = Label(window, text='Current Weather in ' + city)

temp_label = Label(window, text='Temperature')
temp_display = Label(window, text= hourly_data["temperature_2m"])

wind_label = Label(window, text='Wind Speed & Direction')
windspeed_display = Label(window, text= hourly_data["wind_speed_180m"])
winddirection_display = Label(window, text= hourly_data["wind_direction_180m"])

uv_label = Label(window, text='UV Index')
uv_display = Label(window, text= hourly_data["uv_index"] )

humidity_label = Label(window, text='Humidity')
humidity_display = Label(window, text= hourly_data["relative_humidity_2m"])


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