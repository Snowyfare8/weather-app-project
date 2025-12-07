# API Prototype
import openmeteo_requests
import geocoder
import pandas as pd
import requests_cache
from retry_requests import retry
import requests

# Geolocator
ip = geocoder.ip('me')
city = ip.city 
geo_url = "https://geocoding-api.open-meteo.com/v1/search"
geo_params = {"name": city, "count": 1}
geo_res = requests.get(geo_url, params=geo_params).json()

# API 1
cache_session = requests_cache.CachedSession('.cache', expire_after = 3600)
retry_session = retry(cache_session, retries = 5, backoff_factor = 0.2)
openmeteo = openmeteo_requests.Client(session = retry_session)

# API 2 - rework maybe needed           
if "results" in geo_res:
    lat = geo_res["results"][0]["latitude"]
    lon = geo_res["results"][0]["longitude"]

    url = "https://api.open-meteo.com/v1/forecast"
    params = {
        "latitude": lat,
        "longitude": lon,
        "hourly": ["temperature_2m", "relative_humidity_2m", "wind_speed_180m", "wind_direction_180m", "uv_index"],
        "current": ["temperature_2m", "relative_humidity_2m", "is_day", "wind_direction_10m", "wind_speed_10m",
                    "apparent_temperature", "rain", "precipitation", "showers", "snowfall",
                    "weather_code", "cloud_cover", "pressure_msl", "surface_pressure", "dust"],
        "minutely_15": ["temperature_2m", "relative_humidity_2m", "apparent_temperature", "wind_speed_80m", "wind_direction_80m", "is_day"],
	    "timezone": "auto",
	    "forecast_days": 1,
	    "wind_speed_unit": "ms",
        "models": "best_match"
    }
    responses = openmeteo.weather_api(url, params=params)

    response = responses[0]
   # print(f"Coordinates: {response.Latitude()}°N {response.Longitude()}°E")
   # print(f"Elevation: {response.Elevation()} m asl")
   # print(f"Timezone: {response.Timezone()}{response.TimezoneAbbreviation()}")
   # print(f"Timezone difference to GMT+0: {response.UtcOffsetSeconds()}s")

    minutely_15 = response.Minutely15()
    minutely_15_temp = minutely_15.Variables(0).ValuesAsNumpy()
    minutely_15_humidity = minutely_15.Variables(1).ValuesAsNumpy()
    minutely_15_apptemp = minutely_15.Variables(2).ValuesAsNumpy()
    minutely_15_windspeed = minutely_15.Variables(3).ValuesAsNumpy()
    minutely_15_winddirection = minutely_15.Variables(4).ValuesAsNumpy()
    minutely_15_is_day = minutely_15.Variables(5).ValuesAsNumpy()

    minutely_15_data = {"date": pd.date_range(
	    start = pd.to_datetime(minutely_15.Time(), unit = "s", utc = True),
	    end =  pd.to_datetime(minutely_15.TimeEnd(), unit = "s", utc = True),
	    freq = pd.Timedelta(seconds = minutely_15.Interval()),
	    inclusive = "left"
    )}

    minutely_15_data["temperature_2m"] = minutely_15_temp
    minutely_15_data["relative_humidity_2m"] = minutely_15_humidity
    minutely_15_data["apparent_temperature"] = minutely_15_apptemp
    minutely_15_data["wind_speed_80m"] = minutely_15_windspeed
    minutely_15_data["wind_direction_80m"] = minutely_15_winddirection
    minutely_15_data["is_day"] = minutely_15_is_day

    current = response.Current()
    current_temp = current.Variables(0).Value()
    current_humidity = current.Variables(1).Value()
    current_is_day = current.Variables(2).Value()
    current_winddirection = current.Variables(3).Value()
    current_windspeed = current.Variables(4).Value()
    current_apptemp = current.Variables(5).Value()
    current_rain = current.Variables(6).Value()
    current_precipitation = current.Variables(7).Value()
    current_showers = current.Variables(8).Value()
    current_snowfall = current.Variables(9).Value()
    current_weather_code = current.Variables(10).Value()
    current_cloud_cover = current.Variables(11).Value()
    current_pressure_msl = current.Variables(12).Value()
    current_surfpressure = current.Variables(13).Value()
    current_dust = current.Variables(14).Value()

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

    hourly_data["temperature_2m"] = hourly_temp
    hourly_data["relative_humidity_2m"] = hourly_humidity
    hourly_data["wind_speed_180m"] = hourly_windspeed
    hourly_data["wind_direction_180m"] = hourly_winddirection
    hourly_data["uv_index"] = hourly_uvindex

    hourly_dataframe = pd.DataFrame(data = hourly_data)
   # print("\nHourly data\n", hourly_dataframe)

    minutely_15_dataframe = pd.DataFrame(data = minutely_15_data)
   # print("\nMinutely15 data\n", minutely_15_dataframe)

   # print(f"\nCurrent time: {current.Time()}")
   # print(f"Current temperature_2m: {current_temp}")
   # print(f"Current relative_humidity_2m: {current_humidity}")
   # print(f"Current is_day: {current_is_day}")
   # print(f"Current wind_direction_10m: {current_winddirection}")
   # print(f"Current wind_speed_10m: {current_windspeed}")
   # print(f"Current apparent_temperature: {current_apptemp}")
   # print(f"Current rain: {current_rain}")
   # print(f"Current precipitation: {current_precipitation}")
   # print(f"Current showers {current_showers}")
   # print(f"Current snowfall {current_snowfall}")
   # print(f"Current weather code: {current_weather_code}")
   # print(f"Current cloud cover: {current_cloud_cover}")
   # print(f"Current sea level pressure {current_pressure_msl}")
   # print(f"Current surface pressure {current_surfpressure}")
   # print(f"Current dust level {current_dust}")