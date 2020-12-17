from threading import Thread
import time
import sys
import random

# declare a callable class
class MyCallable: # nb this is not a runnable, so we treat it like functional
    def __call__(self, name):
        for i in range(1,50):
            sys.stdout.write(name) # same as print()
            time.sleep( random.random()*0.1 )
        
if __name__ == "__main__":
    #call a function via start() (i.e. functional Threads)
    c3 = MyCallable() # this is like functional - we call the __call_ method
    c2 = MyCallable()
    c1 = MyCallable()

    # call the __call__ cllback
    t1 = Thread(target = c1, args=('M',))
    t2 = Thread(target = c2, args=('N',))
    t3 = Thread(target = c3, args=('P',))

    # now we can start each thread (they all run in the SAME SINGLE process)
    t3.start()
    t2.start()
    t1.start()
    # the main calling thread is blocked until ALL threads terminate
    # the join method is also needed (so we know when they terminate)
    t1.join() # send any output back to the main thread
    t2.join()
    t3.join()
