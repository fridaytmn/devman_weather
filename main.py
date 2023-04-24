import requests


def show_weather_in_london():
    url = 'https://wttr.in/london?nTqu&lang=en'
    try:
        response = requests.get(url)
        response.raise_for_status()
        print(response.text)
    except:
        print('Weather is not avilible')

def show_weather_in_svo():
    url = 'https://wttr.in/svo?nTqmM&lang=en'
    try:
        response = requests.get(url)
        response.raise_for_status()
        print(response.text)
    except:
        print('Weather is not avilible')

def show_weather_in_cherepovec():
    try:
        url = 'https://wttr.in/Череповец?nTqmM&lang=ru'
        response = requests.get(url)
        response.raise_for_status()
        print(response.text)
    except:
        print('Weather is not avilible')
    
show_weather_in_london()
show_weather_in_svo()
show_weather_in_cherepovec()
