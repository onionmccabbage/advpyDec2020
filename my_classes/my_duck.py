# Duck typing
# if it looks like a duck
# walks like a duck
# and sounds like a duck

class Person:
    def Eat(self): pass
    def Drink(self): pass
    def Sleep(self): pass
class Employee(Person):
    def Eat(self): pass
    def Drink(self): pass
    def Sleep(self): pass
class SalesPerson(Employee):
    def Eat(self): pass
    def Drink(self): pass
    def Sleep(self): pass

class Horse:
    def Eat(self): pass
    def Drink(self): pass
    def Sleep(self): pass

def night_out(p):
    p.Drink()
    p.Drink()
    p.Eat()
    p.Drink()
    p.Sleep()

p = Person()
e = Employee()
s = SalesPerson()

night_out(p)
night_out(e)
night_out(s)

h = Horse()
night_out(h)
