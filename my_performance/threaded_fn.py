import sys
import time
import random
from threading import Thread

def myfunc(name):
    for i in range(1,50):
        sys.stdout.write(name) # same as print()
        time.sleep( random.random()*0.1 )
        
if __name__ == "__main__":
    #call a function via start() (i.e. functional Threads)
    t1 = Thread(target=myfunc, args=('A', ))
    t2 = Thread(target=myfunc, args=('B', ))
    t3 = Thread(target=myfunc, args=('C', ))

    # now we can start each thread (they all run in the SAME SINGLE process)
    t1.start()
    t2.start()
    t3.start()
    # the main calling thread is blocked until ALL threads terminate
    # the join method is also needed (so we know when they terminate)
    t1.join() # send any output back to the main thread
    t2.join()
    t3.join()

    # we will not be able to run ANY further code until ALL threads have terminated