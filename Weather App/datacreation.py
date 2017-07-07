import datetime
import urllib.request, urllib.parse, urllib.error
import json
import random
import math

def data_fetch_forecast(complete_forecast_api): #Uses the weather api to return a 5 day forecast based on location [Works w/ help from Stack Exchange]
    url = urllib.request.urlopen(complete_forecast_api) #Opens connection to API
    output = url.read().decode('utf-8') #Encodes API in way that can be read
    raw_forecast_api_dict = json.loads(output) #Assigns all data to a local variable
    url.close() #Ends connection
    return raw_forecast_api_dict

def data_fetch_current(complete_current_api): #Uses the weather api to return current weather based on location [Works w/ help from Stack Exchange]
    url = urllib.request.urlopen(complete_current_api) #Opens connection to API
    output = url.read().decode('utf-8') #Encodes API in way that can be read
    raw_current_api_dict = json.loads(output) #Assigns all data to a local variable
    url.close() #Ends connection
    return raw_current_api_dict
