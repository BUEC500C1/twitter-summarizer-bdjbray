import pyowm
owm=pyowm.OWM('')
observation=owm.weather_at_place('San Francisco, US')
weaher=observation.get_weather()
temperature=weaher.get_temperature('fahrenheit')['temp']
print(temperature)