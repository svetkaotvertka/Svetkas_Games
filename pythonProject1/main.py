from pyowm import OWM

owm = OWM('3ad73919d96fea1f9833c9eef2d1edc4')
mgr = owm.weather_manager()

location = input("В каком городе?:")

observation = mgr.weather_at_place(location)
w = observation.weather

print(w)
