from random import randint
from location import Location
from countries import countries

class Weather():
    def __init__(self, desc, temp, location):
        self.__desc = desc
        self.__temp = temp
        self.location = location # make sure we use the setter method
    @property
    def location(self):
        return self.__location
    @location.setter
    def location(self, new_location):
        # print(type(new_location))
        if type(new_location) == Location:
            self.__location = new_location
        else:
            self.__location = Location('Edinburgh', 'uk')
    @property
    def desc(self):
        return self.__desc
    @desc.setter
    def desc(self, new_desc):
        if type(new_desc) == str and new_desc != '':
            self.__desc = new_desc
    @property
    def temp(self):
        return self.__temp
    @temp.setter
    def temp(self, new_temp):
        if type(new_temp) == int or type(new_temp) == float:
            self.__temp = new_temp
    def __str__(self):
        # output a nicely formatted weather report
        report  = 'The weather in {0}, {1} is {2} at {3:.2f}C'.format(self.location.city, self.location.country, self.__desc, self.__temp)
        return report
    def changeTemp(self):
        # alter the temperature by a small random amount
        tempChange = randint(-5, 5) 
        self.temp += tempChange

if __name__ == '__main__':
    # exercise this module
    l1 = Location('Athlone', 'ie')
    w_ath = Weather('rainy', 9.04, l1)
    l2 = Location('Galway', 'ie')
    w_gal = Weather('windy', 6.70, l2)
    l3 = Location('Kingston', 'jm')
    w_kt = Weather('Sunny', 27.98, l3)
    w_kt.changeTemp()
   
    print(w_ath)
    print(w_gal)
    print(w_kt)

    l4 = 'nonsuch'
    w_default = Weather('rainy', 9.04, l4)
    print(w_default)
