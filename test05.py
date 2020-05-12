import pyowm

owm = pyowm.OWM("494f9cbe3c88fcd543ca91f7c785c67c")

place = input("Please select your city: ")

observation = owm.weather_at_place(place)

weather = observation.get_weather()

print(weather)