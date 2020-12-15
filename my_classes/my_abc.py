# Here we have an Abstract Base Class (ABC)
from abc import ABCMeta, abstractmethod, abstractproperty

class Shape:
    __metaclass__ = ABCMeta # we make this abstract
    @abstractmethod
    def display(self):
        pass
    @property
    @abstractproperty
    def name(self):
        pass

