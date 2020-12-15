from weather import Weather  
from datetime import datetime
from random import randint

# inherit from the Weather class
class WeatherHistorical(Weather):
    def __init__(self, desc, temp, location, timestamp):
        super().__init__(desc, temp, location)
        self.ts = timestamp # direct access is fine
    # override method of parent
    def __str__(self):
        # output a nicely formatted weather report
        report  = 'At {4} the weather in {0}, {1} is {2} at {3:.2f}C'.format(self.location.city, self.location.country, self.desc, self.temp, self.ts)
        return report
    def changeTemp(self):
        # alter the temperature by a small random amount
        tempChange = randint(-5, 5) 
        self.temp += tempChange

if __name__ == '__main__':
    from location import Location
    # exercise this module
    ts = datetime.now()
    l1 = Location('Athlone', 'ie')
    w_ath = WeatherHistorical('rainy', 9.04, l1, ts)
    l2 = Location('Galway', 'ie')
    w_gal = WeatherHistorical('windy', 6.70, l2, ts)
    l3 = Location('Kingston', 'jm')
    w_kt = WeatherHistorical('Sunny', 27.98, l3, ts)
    w_kt.changeTemp()

    print(w_ath)
    print(w_gal)
    print(w_kt)
