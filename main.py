import requests


def show_weather(cities: dict):
    url = 'http://wttr.in/'
    for city in cities.keys():
        response = requests.get(f'{url}{city}', params=cities[city]['params'])
        response.raise_for_status()
        print(response.text)

        
def main():
    cities = {'London': {'params': {'nTqM': '', 'lang': 'ru'}},
              'svo': {'params': {'nTqM': '', 'lang': 'ru'}},
              'Череповец': {'params': {'nTqM': '', 'lang': 'ru'}}
              }
    try:
        show_weather(cities)
    except requests.exceptions.ConnectionError:
        'Weather is not avilible'

        
if __name__ == '__main__':
    main()
