# overload the ADD operator, so it works for trivial times

class Time:
    def __init__(self, h, m):
        self.m = ( h*60 + m ) % (24*60)
    def __add__(self, other):
        return Time(0, self.m + other.m)
    def __str__(self):
        return f'Time is {self.m//60}:{self.m%60}'

class MyLister:
    def __init__(self):
        self.data = 'wxyzabc'
    def __getitem__(self, i):
        return self.data[i]

if __name__ == '__main__':
    t1 = Time(12,30)
    t2 = Time(1, 35)
    t3 = t1 + t2 # call our __add__ method
    print(t3)

    ml = MyLister()
    char = ml[3]
    print(char)

