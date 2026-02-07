# Weather API
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

# Weather API         
if "results" in geo_res:
    lat = geo_res["results"][0]["latitude"]
    lon = geo_res["results"][0]["longitude"]

    # Forecast subAPI
    url = "https://api.open-meteo.com/v1/forecast"
    params = {
        "latitude": lat,
        "longitude": lon,
        "hourly": ["temperature_2m", "relative_humidity_2m", "wind_speed_180m", "wind_direction_180m", "uv_index", "precipitation"],
        "current": ["temperature_2m", "relative_humidity_2m", "is_day", "wind_direction_10m", "wind_speed_10m",
                    "apparent_temperature", "precipitation", "cloud_cover", "pressure_msl", "surface_pressure"],
        "minutely_15": ["temperature_2m", "relative_humidity_2m", "apparent_temperature", "wind_speed_80m", "wind_direction_80m", "precipitation"],
	    "timezone": "auto",
	    "forecast_days": 1,
	    "wind_speed_unit": "ms",
        "models": "best_match"
    }
    responses = openmeteo.weather_api(url, params=params)

    response = responses[0]

    minutely_15 = response.Minutely15()
    minutely_15_temp = minutely_15.Variables(0).ValuesAsNumpy()
    minutely_15_humidity = minutely_15.Variables(1).ValuesAsNumpy()
    minutely_15_apptemp = minutely_15.Variables(2).ValuesAsNumpy()
    minutely_15_windspeed = minutely_15.Variables(3).ValuesAsNumpy()
    minutely_15_winddirection = minutely_15.Variables(4).ValuesAsNumpy()
    minutely_15_precipitation = minutely_15.Variables(5).ValuesAsNumpy()

    minutely_15_data = {"date": pd.date_range(
	    start = pd.to_datetime(minutely_15.Time() + response.UtcOffsetSeconds(), unit = "s", utc = True),
	    end =  pd.to_datetime(minutely_15.TimeEnd() + response.UtcOffsetSeconds(), unit = "s", utc = True),
	    freq = pd.Timedelta(seconds = minutely_15.Interval()),
	    inclusive = "left"
    )}

    minutely_15_data["temperature_2m"] = minutely_15_temp
    minutely_15_data["relative_humidity_2m"] = minutely_15_humidity
    minutely_15_data["apparent_temperature"] = minutely_15_apptemp
    minutely_15_data["wind_speed_80m"] = minutely_15_windspeed
    minutely_15_data["wind_direction_80m"] = minutely_15_winddirection
    minutely_15_data["precipitation"] = minutely_15_precipitation

    current = response.Current()
    current_temp = current.Variables(0).Value()
    current_humidity = current.Variables(1).Value()
    current_is_day = current.Variables(2).Value()
    current_winddirection = current.Variables(3).Value()
    current_windspeed = current.Variables(4).Value()
    current_apptemp = current.Variables(5).Value()
    current_precipitation = current.Variables(6).Value()
    current_cloud_cover = current.Variables(7).Value()
    current_pressure_msl = current.Variables(8).Value()
    current_surfpressure = current.Variables(9).Value()

    response = responses[0]
    hourly = response.Hourly()
    hourly_temp = hourly.Variables(0).ValuesAsNumpy()
    hourly_humidity = hourly.Variables(1).ValuesAsNumpy()
    hourly_windspeed = hourly.Variables(2).ValuesAsNumpy()
    hourly_winddirection = hourly.Variables(3).ValuesAsNumpy()
    hourly_uvindex = hourly.Variables(4).ValuesAsNumpy()
    hourly_precipitation = hourly.Variables(5).ValuesAsNumpy()

    hourly_data = {"date": pd.date_range(
        start = pd.to_datetime(hourly.Time() + response.UtcOffsetSeconds(), unit = "s", utc = True),
        end = pd.to_datetime(hourly.TimeEnd() + response.UtcOffsetSeconds(), unit = "s", utc = True),
        freq = pd.Timedelta(seconds = hourly.Interval()),
        inclusive = "right"
    )}

    hourly_data["temperature_2m"] = hourly_temp
    hourly_data["relative_humidity_2m"] = hourly_humidity
    hourly_data["wind_speed_180m"] = hourly_windspeed
    hourly_data["wind_direction_180m"] = hourly_winddirection
    hourly_data["uv_index"] = hourly_uvindex
    hourly_data["precipitation"] = hourly_precipitation

    hourly_dataframe = pd.DataFrame(data = hourly_data)

    minutely_15_dataframe = pd.DataFrame(data = minutely_15_data)

    print(f"Current precipitation: {current_precipitation}")
