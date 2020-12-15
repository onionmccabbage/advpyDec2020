from my_abc import Shape


class Circle(Shape):
    def __init__(self, name):
        self.__name = name # this mangles the proerpty identifier, so it becomes _Circle__name
    def display(self):
        print(f'Circle {self.name}')
    @property
    def name(self):
        return self.__name

if __name__ == '__main__':
    c = Circle('round')
    # s = Shape() # we would not normlly intantiate an ABC
    # s.display()
    c.display()
    print(c.name) # access the name property method

    # we can expore features of clsses
    print( c.__module__, c.__dict__, c.__class__ )
