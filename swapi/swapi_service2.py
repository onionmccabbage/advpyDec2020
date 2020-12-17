# a service to access https://swapi.dev/api
import sys
sys.path.append('d:/advpy/libs/')
import requests
from threading import Thread

class SwapiService(Thread):
    def __init__(self, category, id):
        Thread.__init__(self)
        self.category = category
        self.id = id
        self.__return = 'return'
    def run(self):
        url = "https://swapi.dev/api/{}/{}".format(self.category, self.id)
        print(url)
        response = requests.get(url)
        self.__return = response.text
    def join(self):
        Thread.join(self)
        return self.__return

if __name__ == "__main__":
    SwapiService().__init__()