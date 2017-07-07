import datetime
import urllib.request, urllib.parse, urllib.error
import json

def get_max_temps(raw_api_dict): #Get dict of max temps
  day_max_stats = {} #Empty dict
  for i in range(len(raw_api_dict['list'])): #Iterates through all the data
    date_string = raw_api_dict['list'][i]['dt_txt'][:10] #Slices just the date part of the date-time string
    if date_string in day_max_stats: #Checks if it is in the dict
      current_max = day_max_stats[date_string]#If so, its (key) current value is equal to current_max
      new_temp = raw_api_dict['list'][i]['main']['temp_max'] #Any string that matches up with the date will have its max temp taken
      if new_temp > current_max: #If new_temp is greater than current_max
        day_max_stats[date_string] = new_temp #The new_temp is the current max
      else:
        continue #If not then move on
    else:
      day_max_stats[date_string] = raw_api_dict['list'][i]['main']['temp_max'] #If the date in not in the dict, it will be added with its current max temp value
  return day_max_stats #Returns the max temp dict

def get_min_temps(raw_api_dict): #Get dict of min temps
  day_min_stats = {} #Empty dict
  for i in range(len(raw_api_dict['list'])): #Iterates through all the data
    date_string = raw_api_dict['list'][i]['dt_txt'][:10] #Slices just the date part of the date-time string
    if date_string in day_min_stats: #Checks if it is in the dict
      current_min = day_min_stats[date_string] #If so, its (key) current value is equal to current_min
      new_temp = raw_api_dict['list'][i]['main']['temp_min'] #Any string that matches up with the date will have its min temp taken
      if new_temp < current_min:
        day_min_stats[date_string] = new_temp #The new_temp is the current_min
      else:
        continue #If not then move on
    else:
      day_min_stats[date_string] = raw_api_dict['list'][i]['main']['temp_min'] #If the date in not in the dict, it will be added with its current min temp value
  return day_min_stats #Returns the min temp dict

def get_humidity(raw_api_dict): #Get dict of humidities
  humidity_stats = {}  #Empty dict
  for i in range(len(raw_api_dict['list'])): #Iterates through all the data
    date_string = raw_api_dict['list'][i]['dt_txt'][:10] #Slices just the date part of the date-time string
    if date_string in humidity_stats: #Checks if it is in the dict
      current_humidity = humidity_stats[date_string]  #If so, its (key) current value is equal to current_humidity
      new_humidity = raw_api_dict['list'][i]['main']['humidity'] #Any string that matches up with the date will have its 'humidity' taken
      if new_humidity > current_humidity:
        humidity_stats[date_string] = new_humidity #The new_humidity is the humidity
      else:
        continue #If not then move on
    else:
      humidity_stats[date_string] = raw_api_dict['list'][i]['main']['humidity'] #If the date in not in the dict, it will be added with its current humidity value
  return humidity_stats #Returns humidity dict

def get_wind_speed(raw_api_dict): #Get dict of windspeeds
  wind_speed_stats = {} #Empty dict
  for i in range(len(raw_api_dict['list'])): #Iterates through all the data
    date_string = raw_api_dict['list'][i]['dt_txt'][:10] #Slices just the date part of the date-time string
    if date_string in wind_speed_stats: #Checks if it is in the dict
      max_wind_speed = wind_speed_stats[date_string] #If so, its (key) current value is equal to max_wind_speed
      new_wind_speed = raw_api_dict['list'][i]['wind']['speed'] #Any string that matches up with the date will have its 'windspeed' taken
      if new_wind_speed > max_wind_speed:
        wind_speed_stats[date_string] = new_wind_speed #The new_wind_speed is the current windspeed
      else:
        continue #If not then move on
    else:
      wind_speed_stats[date_string] = raw_api_dict['list'][i]['wind']['speed'] #If the date in not in the dict, it will be added with its current windspeed value
  return wind_speed_stats #Returns windspeed dict

def today_weather_description(raw_api_dict): #Returns the given weather description at the current time
  weather_description = raw_api_dict['weather'][0]['description']
  return weather_description

def current_temp(raw_api_dict): #Returns the temperature at the current time
  current_temperature = raw_api_dict['main']['temp']
  return current_temperature

def get_current_humidity(raw_api_dict): #Returns the given humidity at the current time
  current_humidity = raw_api_dict['main']['humidity']
  return current_humidity

def get_current_windspeed(raw_api_dict): #Returns the given windspeed at the current time
  current_windspeed = raw_api_dict['wind']['speed']
  return current_windspeed

def get_sunrise(raw_api_dict): #Pulls the time of sunrise for the current day
  timestamp = raw_api_dict['sys']['sunrise'] #Get sunrise time in a UNIX Timestamp
  sunrise_time = datetime.datetime.fromtimestamp(timestamp) #Takes the timestamp, converts it, and assigns it to a variable
  sunrise = sunrise_time.strftime('%H:%M:%S') #Formats time in GMT
  return sunrise

def get_sunset(raw_api_dict): #Pulls the time of sunset for the current day
  timestamp = raw_api_dict['sys']['sunset'] #Get sunset time in a UNIX Timestamp
  sunset_time = datetime.datetime.fromtimestamp(timestamp) #Takes the timestamp, converts it, and assigns it to a variable
  sunset = sunset_time.strftime('%H:%M:%S') #Formats time in GMT
  return sunset

def get_name(raw_api_dict): #Returns name with proper spelling and grammar
  name = raw_api_dict['city']['name']
  return name
