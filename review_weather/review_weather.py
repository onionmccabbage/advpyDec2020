# pip install --target=D:\advpy\libs requests --ignore-installed
import requests
from datetime import datetime

class WeatherGetter:
    def __init__(self, city='edinburgh', country='uk'):
        # super().__init__()
        self.city    = city
        self.country = country
        self.APIkey  = 'APPID=48f2d5e18b0d2bc50519b58cce6409f1'

    def getWeather(self):
        url_str = 'http://api.openweathermap.org/data/2.5/weather?q={},{}&units=metric&{}'
        url = url_str.format(self.city, self.country, self.APIkey)
        response = requests.get(url)
        data  = response.json()
        if 'main' in data:
            # self.temperature = data['main']['temp']
            return data       

def main(city, country):
    weatherGetter = WeatherGetter(city, country)
    weather = weatherGetter.getWeather()
    d = weather['weather'][0]['description']
    t = weather['main']['temp']
    n = weather['name']
    ws = weather['wind']['speed']
    wd = weather['wind']['deg']
    report_string = '''Description: {}
Temperature: {:.0f}°C in {}, {}
The wind speed is {} coming from {}° 
'''.format(d, t, n, country, ws, wd)
    report_d = {'desc':d , 'temperature':t , 'city':n , 'country':country, 'wind_speed':ws, 'wind_direction':wd}
    print(report_string)
    # persist in text file
    with open("reports.txt", 'a') as r:
        for line in report_string:
            r.write(line)

if __name__ == '__main__':
    city = input('Choose a city:')
    country = input('choose a country:')
    main(city, country)