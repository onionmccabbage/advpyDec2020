# classes aim to encapsulate features of a concept that matter
# leaving out irrelevant parts

# classes have properties (things they have)
# and methods (things they can do)

# here is a person taking name and email
class Person(object): # by default we inherit from 'object'
    def __init__(self, name, email): # this is like a constructor. all classes MUST have __init__ and self
        self.__name = name # these are now properties of this class
        self.__email = email # __ mangles the property to prevent access
    def showMe(self): # all methods must include self
        print('Name: {} Email: {}'.format(self.__name, self.email))
    def get_name(self): # this should return the name
        return self.__name
    def set_name(self, new_name):
        if type(new_name)== str and new_name != '':
            self.__name = new_name
        else:
            self.__name = 'NA'
    def get_email(self): # this should return the email
        return self.__email
    def set_email(self, new_email):
        if type(new_email)== str and new_email != '':
            self.__email = new_email
        else:
            self.__email = 'NA'
    name = property(get_name, set_name)    # this makes 'name' a property of the class
    email = property(get_email, set_email) # this makes 'email' a property of the class

# inheritance
class Coder(Person): # here our Coder class inherits from the Person class
    def __init__(self, name, email, languages):
        super().__init__(name, email) # this calls the parent class __init__ method
        self.__languages = languages
    # we can declare accessor and mutator methods for properties (in this case, 'languages')
    def get_languages(self):
        return self.__languages
    def set_languages(self, list_of_languages):
        # check it's a list
        if type(list_of_languages) == 'list':
            self.__languages = list_of_languages
        else:
            pass # don't make any changes
    # make these getter and setter methods behave as a property
    languages = property(get_languages, set_languages)
    # if we needed to  we could write a new 'showMe()' method

if __name__ == '__main__':
    # create instances of our classes
    fred = Person('Fred', 'f@d.ie')
    fred.name='stringy'
    fred.set_name('oobly') # we could use the setter method directly
    fred.__name = False # this does NOT actually mutate the __name member
    fred.showMe()
    # even with property mangling we CAN still ccess the__name
    print(fred._Person__name) # direct access to the property
    # and now a coder
    ada = Coder('Ada', 'a@b.ie', ['Python', 'ECMASCript', 'Ada'])
    ada.showMe()