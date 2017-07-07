from datetime import *
import urllib.request, urllib.parse, urllib.error
import json
import time
import pygal
from pprint import pprint
from datacreation import *
from urlcreation import *
from tempinfo import *

today = datetime.datetime.now()
current_date = today.strftime("%Y-%m-%d") # Today's Date
tomorrow = today + datetime.timedelta(1)
tomorrow_date = tomorrow.strftime("%Y-%m-%d") # Tomorrow's Date
final = today + datetime.timedelta(4)
final_date = final.strftime("%Y-%m-%d") # Last Date that can be accessed in the forecast
continues = ['yes', 'Yes', 'y', 'Y'] #List of continue commands
stops = ['no', 'No', 'n', 'N'] #List of end commands
fahrenheit_symbol = '\xb0' + 'F' #Creates a fahrenheit symbol

while True:

    city = input(">>> Enter a city name (With no spaces):")
    country = input(">>> Enter the country where the city is found (also no spaces):")
    location = URL(city, country) #Creates a location from user input using URL class
    new_forecast_url = URL.create_forecast_url(location)
    raw_forecast_data = data_fetch_forecast(new_forecast_url)
    new_current_url = URL.create_current_url(location)
    raw_current_data = data_fetch_current(new_current_url)
    print("Downloading...")
    print('-'*40)
    time.sleep(5)
    print("Data Located")
    print("-"*40)

    while True:

      min_temp_data = get_min_temps(raw_forecast_data)
      max_temp_data = get_max_temps(raw_forecast_data)
      humidity_data = get_humidity(raw_forecast_data)
      wind_speed_data = get_wind_speed(raw_forecast_data)
      current_description = today_weather_description(raw_current_data)
      current_temperature = current_temp(raw_current_data)
      current_humidity = get_current_humidity(raw_current_data)
      current_windspeed = get_current_windspeed(raw_current_data)
      sunrise = get_sunrise(raw_current_data)
      sunset = get_sunset(raw_current_data)
      name = get_name(raw_forecast_data)


      decision = input(">>> Please choose an Option 1 - 6 for different weather information. If you wish to know more about each option, please type 'help'. When finished, type 'done'.")

      if decision == 'Option 1' or decision == 'option 1' or decision == '1':#Prints out today's forecast
        for key, value in min_temp_data.items(): #Checks for date in list of minimum temps and returns that day's min temp
          if current_date == key:
            today_min = value
        for key, value in max_temp_data.items(): #Checks for date in list of maximum temps and returns that day's max temp
          if current_date == key:
            today_max = value
        for key, value in humidity_data.items(): #Checks for date in list of minimum temps and returns that day's min temp
          if current_date == key:
            today_humidity = value
        for key, value in wind_speed_data.items(): #Checks for date in list of minimum temps and returns that day's min temp
          if current_date == key:
            today_wind_speed = value
        todays_info = ("-" * 40) + "\n" + "Today's Weather in " + name + ", " + country + " on " + current_date + ":" + "\n" + "Sunrise: " + str(sunrise) + " AM GMT" + '\n' + "Sunset: " + str(sunset) + " PM GMT" + "\n" + "Maximum Temperature: " + str(today_max) + " " + fahrenheit_symbol + "\n" + "Minimum Temperature: " + str(today_min) + " " + fahrenheit_symbol + "\n" + "Max Humidity: " + str(today_humidity) + "%" + "\n" + "Wind Speed: " + str(today_wind_speed) + " mph" + "\n" + ("-" * 40)
        print(todays_info)
        file_saving = input("Would you like to save your data:")
        if file_saving in continues: #Allows file saving
          name_file = input("What would you like to name your file (please end all file names with .txt):")
          file = open(name_file, 'w')
          file.write(todays_info)
          file.close()
        print('-'*40)



      if decision == 'Option 2' or decision == 'option 2' or decision == '2':#Prints out tomorrow's forecast
        for key, value in min_temp_data.items(): #Checks for date in list of minimum temps and returns that day's min temp
          if tomorrow_date == key:
            today_min = value
        for key, value in max_temp_data.items(): #Checks for date in list of maximum temps and returns that day's max temp
          if tomorrow_date == key:
            today_max = value
        for key, value in humidity_data.items(): #Checks for date in list of minimum temps and returns that day's min temp
          if tomorrow_date == key:
            today_humidity = value
        for key, value in wind_speed_data.items(): #Checks for date in list of minimum temps and returns that day's min temp
          if tomorrow_date == key:
            today_wind_speed = value
        tomorrows_info = ("-" * 40) + "\n" + "Predicted Weather in " + name + ", " + country + " on " + tomorrow_date + ":" + "\n" + "Predicted Maximum Temperature: " + str(today_max) + " " + fahrenheit_symbol + "\n" + "Predicted Minimum Temperature: " + str(today_min) + " " + fahrenheit_symbol + "\n" + "Predicted Max Humidity: " + str(today_humidity) + "%" + "\n" + "Predicted Wind Speed: " + str(today_wind_speed) + " mph" + "\n" + ("-" * 40)
        print(tomorrows_info)
        file_saving = input("Would you like to save your data:")
        if file_saving in continues: #Allow file saving
          name_file = input("What would you like to name your file (please end all file names with .txt):")
          file = open(name_file, 'w')
          file.write(tomorrows_info)
          file.close()
        print('-'*40)


      if decision == 'Option 3' or decision == 'option 3' or decision == '3': #Prints out current info on a location
        current_info = ('-' * 40) + "\n" + "Current weather in " + name + ", " + country + ":" + "\n" + "Current Overhead: " + current_description + "\n" + "Current Temperature: " + str(current_temperature) + " " + fahrenheit_symbol + '\n' + "Current Humidity: " + str(current_humidity) + '%' + "\n" + "Current Wind Speed: " + str(current_windspeed) + " mph" + "\n" + ('-'*40)
        print(current_info)
        if current_temperature >= 70 and current_temperature < 80:
          print("I would recommend wearing shorts and a t-shirt. But its up to you...")
          print('-'*40)
        if current_temperature >= 666:
          print("Ummmmmmmm....")
          print('-'*40)
        file_saving = input("Would you like to save your data:")
        if file_saving in continues: #Allows file saving
          name_file = input("What would you like to name your file (please end all file names with .txt):")
          file = open(name_file, 'w')
          file.write(current_info)
          file.close()
        print('-'*40)

      if decision == 'Option 4' or decision == 'option 4' or decision == '4':#Prints out five day forecast of max temps
        temperature_chart = pygal.Bar(human_readable=True, legend_at_bottom=True) #Creates bar chart
        temperature_chart.title = "Maximum Temperatures for Five Days"
        for key, value in max_temp_data.items(): #Adds to the chart
          temperature_chart.add('Maximum Temp for ' + key, value)
        temperature_chart.render_to_file('ages.svg')
        print('-'*40)

      if decision == 'Option 5' or decision == 'option 5' or decision == '5':#Prints out five day forecast of min temps
        temperature_chart = pygal.Bar(human_readable=True, legend_at_bottom=True) #Creates bar chart
        temperature_chart.title = "Minimum Temperatures for Five Days"
        for key, value in min_temp_data.items(): #Adds to the chart
          temperature_chart.add('Minimum Temp for ' + key, value)
        temperature_chart.render_to_file('ages.svg')
        print('-'*40)

      if decision == 'Option 6' or decision == 'option 6' or decision == '6':
        print(raw_forecast_data)

      if decision == 'done' or decision == 'Done': #Allows user to end looking at all data in the chosen area
        print("-" * 40)
        break

      if decision == 'help' or decision == 'Help': #Return list of commands that may be inputted
        print("-" * 40)
        print("Option 1: Returns overall information about the weather in your chosen location" + "\n" + "Option 2: Returns tomorrow's weather information about your chosen area" + "\n" + "Option 3: Returns current weather information about your chosen area" + "\n" + "Option 4: Shows the maximum temperatures of the next upcoming days" + "\n" + "Option 5: Shows the minimum temperatures of the next upcoming days" + "\n" + "Option 6: Prints out all data for a location" + '\n' + "Help: Displays this information once more" + "\n" + "Done: Finishes utilizing data from this one location")
        print("-" * 40)

    new_location = input(">>> Would you like to check a new location:") #Allow User to pick new location and start over there
    if new_location in continues:
      print("-"*40)
      continue
    else: #If not, end program
      print("Have a great day!")
      break
