# this is main.py
import sys
import json
from swapi_service2 import SwapiService
from people import People
from vehicles import Vehicles
from planets import Planets
from species import Species
from threading import Thread
from timeit import default_timer

class Menu:
    # categories = ('people', 'planets', 'species', 'vehicles')
    def __init__(self):
        self.menu_choices = {
            "0":self.showMetrics,
            "1":self.getPeople,
            "2":self.getVehicles,
            "3":self.getPlanets,
            "4":self.getSpecies,
            "5":self.quit
        }
    def showMenu(self):
        print('''Choose a category (or quit):
        0: see metrics
        1: get people
        2: get vehicles
        3: get planets
        4: get species
        5: quit
        ''')
    def run(self):
        while True:
            self.showMenu()
            choice = input('option? ')
            action = self.menu_choices.get(choice)
            if action:
                action()
            else:
                print("{} is not a valid option".format(choice))
    def showMetrics(self):
        with open('swapi_metrics', 'rb') as fin:
            metrics = fin.readlines()
            print(metrics)
    def getId(self):
        self.which_id = input('which number? ')
        # we should check an int was entered
        return self.which_id
    def callServiceThread(self):
        start = default_timer()
        self.getId() # now we will have an id in self.which_id
        # spawn a runnable thread
        thr = SwapiService(self.category, self.which_id)
        thr.start()
        result_j = thr.join()
        self.result_d = json.loads(result_j)
        # print(result_d)
        end = default_timer()
        delta = end-start
        metric = bytes(f'Time to access API service: {delta} seconds', 'utf-8')
        with open('swapi_metrics', 'ab') as fout:
            fout.write(metric)
    def getPeople(self):
        self.category = 'people'
        self.callServiceThread()
        self.people = People(self.result_d['name'], self.result_d['height'])
        print ("Name: {} Height: {}cm".format(self.people.name, self.people.height))
    def getPlanets(self):
        self.category = 'planets'
        self.callServiceThread()
        start = default_timer()
        self.planets = Planets(self.result_d['name'], self.result_d['population'])
        print ("Name: {} Population: {}".format(self.planets.name, self.planets.population))
        end = default_timer()
        delta = end-start
        metric = bytes(f'Time to create instance: {delta} seconds', 'utf-8')
        with open('swapi_metrics', 'ab') as fout:
            fout.write(metric)
    def getSpecies(self):
        self.category = 'species'
        self.callServiceThread()
        self.species = Species(self.result_d['name'], self.result_d['classification'])
        print ("Name: {} Classification: {}".format(self.species.name, self.species.classification))
    def getVehicles(self):
        print('not currently working')
    def quit(self):
        sys.exit(0)

if __name__ == "__main__":
    Menu().run()