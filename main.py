import json
import urllib.request
import os

first_url = "http://api.openweathermap.org/data/2.5/weather?q="
second_url = "&APPID=34646a428c9b333a6b1d2d06ccf9bc41&units=imperial"
location = ""
while True:
	location = input("Enter city name: ")
	if len(location) < 1:
		print("\n","==== No Name Entered ====", "\n")
		continue
	else:
		url = first_url + location + second_url
		os.system("cls")
		break

while True:
	try:
	    print("Retrieving...")
	    uh = urllib.request.urlopen(url)
	    data = uh.read()
	    js = json.loads(data.decode("utf-8"))
	    print("Retrieval successful")
	except:
		print("==== Failure to Retrieve ====")
		usr=input()

	current_temp = js["main"]["temp"]
	wind_speed = js["wind"]["speed"]
	humidity = js["main"]["humidity"]
	description = js["weather"][0]["description"]
	pressure = js["main"]["pressure"]

	current_temp = round(current_temp)
	wind_speed = round(wind_speed)


	print("The weather of", location, "airport is:\n")
	print("Current atmospheric description:", description)
	print("Current Temperature:", current_temp, "fahrenheit")
	print("Humidity:", humidity, "%")
	print("Wind speed:", wind_speed, "mph")
	print("Atmospheric Pressure:", pressure, "hPa")
	print("")

	refresh = input("To refresh press ENTER\n")
	if len(refresh) < 1:
		os.system("cls")
		continue
	else:
		break