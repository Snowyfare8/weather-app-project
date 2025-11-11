# API Prototype
import openmeteo_requests

import pandas as pd
import requests_cache
from retry_requests import retry

# API 1
cache_session = requests_cache.CachedSession('.cache', expire_after = 3600)
retry_session = retry(cache_session, retries = 5, backoff_factor = 0.2)
openmeteo = openmeteo_requests.Client(session = retry_session)

# API 2

weather_url = "https://api.open-meteo.com/v1/forecast"
weather_params = {
    "latitude": 52.52,    
    "longitude": 13.41,
    "hourly": ["temperature_2m","relative_humidity_2m","wind_speed_180m","wind_direction_180m"],
}
responses = openmeteo.weather_api(weather_url, params=weather_params)
    
response = responses[0]
print(f"Coordinates: {response.Latitude()}°N {response.Longitude()}°E")
print(f"Elevation: {response.Elevation()} m asl")
print(f"Timezone difference to GMT+0: {response.UtcOffsetSeconds()}s")

# Hourly Variables
hourly = responses.Hourly()
hourly_temperature_2m = hourly.variables(0).ValuesAsNumpy()
hourly_relative_humidity_2m = hourly.variables(1).ValuesAsNumpy()
hourly_wind_speed_180m = hourly.variables(2).ValuesAsNumpy()
hourly_wind_direction_180m = hourly.variables(3).ValuesAsNumpy()
hourly_uv_index = hourly.variables(4).ValuesAsNumpy()

hourly_data = {"date": pd.date_range(
        start = pd.to_datetime(hourly.Time(), unit = "s", utc = True),
        end = pd.to_datetime(hourly.Timeend(), unit = "s", utc = True),
        freq = pd.Timedelta(seconds = hourly.Interval()),
        inclusive = "left"
)}

# Assign hourly data to hourly variables
hourly_data["temperature_2m"] = hourly_temperature_2m
hourly_data["relative_humidity_2m"] = hourly_relative_humidity_2m
hourly_data["wind_speed_180m"] = hourly_wind_speed_180m
hourly_data["wind_direction_180m"] = hourly_wind_direction_180m
hourly_data["uv_index"] = hourly_uv_index

hourly_dataframe = pd.DataFrame(data = hourly_data)
print("\nHourly data\n", hourly_dataframe)