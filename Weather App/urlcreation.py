import datetime
import urllib.request, urllib.parse, urllib.error
import json

class URL(object):

  def __init__(self, city, country): #Creates a location from User Input
    self.city = city
    self.country = country

  def create_forecast_url(self): #Creates a URL for a forecast from User Input
    api_key = 'abc7f63e2c3d77dcde7e622c653c5d20' #Specific Key for program to access
    units = 'imperial' #Fahrenheit
    api = 'http://api.openweathermap.org/data/2.5/forecast?q=' #Base of the forecast URL
    complete_forecast_api = api + self.city + ',' + self.country + '&mode=json&units=' + units + '&appid=' + api_key
    return complete_forecast_api #Complete URL is returned

  def create_current_url(self): #Creates a URL for current weather from User Input
    api_key = 'abc7f63e2c3d77dcde7e622c653c5d20' #Specific Key for program to access
    units = 'imperial' #Fahrenheit
    api = 'http://api.openweathermap.org/data/2.5/weather?q=' #Base of current weather URL
    complete_current_api = api + self.city + ',' + self.country + '&mode=json&units=' + units + '&appid=' + api_key
    return complete_current_api #Complete URL is returned
