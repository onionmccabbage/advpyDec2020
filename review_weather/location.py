from countries import countries

class Location():
    def __init__(self, city, country='ie'): # sensible default for country
        self.__city = city
        self.country = country # use the setter method
    def __str__(self):
        loc = '{} {}'.format(self.__city, self.__country)
        return loc
    @property
    def city(self):
        return self.__city
    @city.setter
    def city(self, new_city):
        if type(new_city) == str and new_city != '':
            self.__city = new_city
    @property
    def country(self):
        return self.__country
    @country.setter
    def country(self, new_country):
        if new_country in countries:
            self.__country = new_country
        else:
            self.__country = 'uk' # default
if __name__ == '__main__':
    l1 = Location('Edinburgh', 'uk')
    l2 = Location('Galway', 'ie')
    l3 = Location('Kingston', 'jm')
    l4 = Location('Begonia', '__')
    print(l4)