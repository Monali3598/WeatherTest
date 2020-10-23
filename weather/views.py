import json

from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.decorators import api_view
import requests
from django.core.cache import cache
from django.conf import settings
from django.core.cache.backends.base import DEFAULT_TIMEOUT

CACHE_TTL = getattr(settings, 'CACHE_TTL', DEFAULT_TIMEOUT)

def get_data(city, country_code):
    result = {"meta_data": {}, "data": {}}
    if f"{city}_{country_code}" in cache:
        # get results from cache

        print("Data from Cache")
        response_json = cache.get(f"{city}_{country_code}")
        result["meta_data"]["Data_From_Cache"] = True
        result["data"].update(response_json)
        print(type(response_json),"from cache")

    else:
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city},{country_code}&appid=1508a9a4840a5574c822d70ca2132032"

        response_json = requests.get(url).json()
        result["meta_data"]["Data_From_Cache"]=False
        result["data"].update(response_json)

        # store data in cache
        cache.set(f"{city}_{country_code}",response_json, timeout=CACHE_TTL)
    return result

@api_view(['GET'])
def get_result(request, city, country_code):
    result= get_data(city, country_code)
    return HttpResponse(json.dumps(result,indent=2),content_type="application/json", status=status.HTTP_201_CREATED)

# @api_view(['GET'])
# def get_forecast_data(request,city_name,count):
#     result1 = {"meta_data": {}, "data": {}}
#     if f"{city_name}_{count}" in cache:
#         response_json_forecast = cache.get(f"{city_name}_{count}")
#         result1["meta_data"]["Data_From_Cache"] = True
#         result1["data"].update(response_json_forecast)
#
#     else:
#         url1 = url=f"api.openweathermap.org/data/2.5/forecast/daily?q={city_name}&cnt={count}&appid=1508a9a4840a5574c822d70ca2132032"
#         response_json_forecast = requests.get(url1).json()
#         result1["meta_data"]["Data_From_Cache"] = False
#         result1["data"].update(response_json_forecast)
#
#         # store data in cache
#         cache.set(f"{city_name}_{count}", response_json_forecast, timeout=CACHE_TTL)
#     return HttpResponse(json.dumps(result1,indent=2),content_type="application/json", status=status.HTTP_201_CREATED)






