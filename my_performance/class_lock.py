from threading import Lock, Thread
import sys
import random
import time

lock = Lock()
c1 = 0 # these are in the global namespace, i.e. they belong to the module
c2 = 0

class AnyClass:
    def __call__(self, name):
        # we need access to the global values
        global lock, c1, c2
        for i in range(0, 20*1000*100): # we can experiment with these numbers
            c1 +=1
            lock.acquire()
            c2 +=1
            lock.release()

if __name__ == "__main__":
    a1 = AnyClass()
    a2 = AnyClass()
    a3 = AnyClass()
    a4 = AnyClass()

    # declare callbacks 
    t1 = Thread(target=a1, args=('1'))
    t2 = Thread(target=a2, args=('2'))
    t3 = Thread(target=a3, args=('3'))
    t4 = Thread(target=a4, args=('4'))

    t1.start()
    t2.start()
    t3.start()
    t4.start()

    t1.join()
    t2.join()
    t3.join()
    t4.join()

    print(c1, c2)



