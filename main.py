sudo pip3 install pyowm 
import pyowm
degree_sign=u'\N{DEGREE SIGN}'
owm=pyowm.OWM('')
loc=input("please choose a city:")
observation=owm.weather_at_place(loc)
weaher=observation.get_weather()
temperature=weaher.get_temperature('fahrenheit')['temp']
wind=weaher.get_wind('miles_hour')['speed']
#direction=weaher.get_wind()['deg']
humidity=weaher.get_humidity()
status=weaher.get_status()
print(f'The weather graph of {loc} airport is below!')
print('---------------------------------------')
print(f'The local weather status is {status}')
print(f'The temperature at the location is {temperature}{degree_sign}')
print(f'The wind speed is {wind} ')
print(f'The humidity is {humidity}%')

