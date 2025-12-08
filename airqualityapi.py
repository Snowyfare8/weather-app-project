# Air Quality API
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

if "results" in geo_res:
    lat = geo_res["results"][0]["latitude"]
    lon = geo_res["results"][0]["longitude"]

    # Air Qual subAPI
    url = "https://air-quality-api.open-meteo.com/v1/air-quality"
    params = {
        "latitude": lat,
        "longitude": lon,
        "current": ["dust", "european_aqi", "pm10", "pm2_5", "carbon_monoxide", "nitrogen_dioxide", "sulphur_dioxide", "ozone"],
	    "timezone": "auto",
	    "forecast_days": 1,
    }
    responses = openmeteo.weather_api(url, params=params)

    response = responses[0]
    current = response.Current()
    current_dust = current.Variables(0).Value()
    current_euroaqi = current.Variables(1).Value()
    current_pm10 = current.Variables(2).Value()
    current_pm2_5 = current.Variables(3).Value()
    current_co = current.Variables(4).Value()
    current_no2 = current.Variables(5).Value()
    current_so2 = current.Variables(6).Value()
    current_o3 = current.Variables(7).Value()

