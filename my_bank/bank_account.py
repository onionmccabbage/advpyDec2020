# import
import abc

# classes
class AttemptExceedOverdraft(Exception):
    pass # all we need is a name for our custom exception

class Transaction: # object
    __metaclass__ = abc.ABCMeta # this is now abstract
    def __init__(self,amount):
        self.amount = amount
    @property
    @abc.abstractproperty
    def value(self):
        pass
    def __str__(self):
        return f'Transaction of {self.value}'
# concrete uses of the abstract Tranaction
class Deposit(Transaction):
    @property
    def value(self):
        return self.amount # positive amount
class Withdraw(Transaction):
    @property
    def value(self):
        return -self.amount # negative amount

class PositiveNumber:
    def __init__(self, name):
        self.name = name # we can asign a name to our positive number property
    def __get__(self, obj, objtype): # descriptor
        return obj.__dict__[self.name]
    def __set__(self, obj, value):
        if value <0:
            raise ValueError(f'{value} cannot be negative')
        obj.__dict__[self.name] = value

class BankAccount:
    balance = PositiveNumber('balance')
    def __init__(self, name, balance):
        self.__name, self.balance = name, balance
        self.overdraft_limit = 0
        self.transactions = [] # start with no transactions
    @property
    def name(self):
        return self.__name
    @name.setter 
    def name(self, new_name):
        # we should validate...
        self.__name = new_name
    def deposit(self, amount):
        self.balance += amount # do we need to overload the + operator?
        self.transactions.append(Deposit(amount))
    def withdraw(self, amount):
        try:
            self.balance -= amount
        except: # ValueError
            raise # this will cascade the exception built in to the PositiveNumber
        else: # there was no exception!
            self.transactions.append( Withdraw(amount) )
        return
    # we need bank statements
    def statement(self): # or __str__
        return (f'{self.__name} balance is {self.balance}')
    # we need to access the transactions
    def __getitem__(self, item): # __getitem__ allows acces to ANY member of the class dict
        return self.transactions[item] # we have overridden __getitem__
    # we an override incremental-add +=
    def __iadd__(self, amount):
        self.balance += amount
        return self

class SavingAccount(BankAccount):
    def __init__(self, name, balance, rate):
        BankAccount.__init__(self, name, balance)
        self.rate = rate
    def statement(self):
        return (f'{self.__name} balance is {self.balance} and rate is {self.rate}')

# immediate code
if __name__ == '__main__':
    my_acc = BankAccount('Joan', 500)
    print( my_acc.statement() )
    other_acc = BankAccount('Mo', 100)
    try:
        other_acc.withdraw(500)
    except ValueError as ve:
        print(f'Failed to withdraw: {ve}')

    print( other_acc.statement() )

    # deposit and withdraw
    my_acc.deposit(50)
    my_acc.withdraw(25)
    # make use of the accesssors via dictionary __getitem__
    print( my_acc[0], my_acc[1] )