import sys
import time
import random
from threading import Thread

# Each thread has it's own stack
# each thread SHARES the Heap, any Statics and any resources e.g. files
# the Python kernel (single process) schedules the threads

# declare a runnable class
class MyRunnable(Thread): # if we extend the Thread class, we MUST provide a run method
    def __init__(self, name):
            Thread.__init__(self)
            self.name = name
    def run(self):    
        for i in range(1,50):
            sys.stdout.write(self.name) # same as print()
            time.sleep( random.random()*0.1 )
        
if __name__ == "__main__":
    #call a function via start() (i.e. functional Threads)
    t3 = MyRunnable('Z') # this is more flexible than functional threads
    t2 = MyRunnable('Y')
    t1 = MyRunnable('X')

    # now we can start each thread (they all run in the SAME SINGLE process)
    # calling start invokes teh run() method of a runnable class
    t3.start()
    t2.start()
    t1.start()
    # the main calling thread is blocked until ALL threads terminate
    # the join method is also needed (so we know when they terminate)
    t1.join() # send any output back to the main thread
    t2.join()
    t3.join()

    # we will not be able to run ANY further code until ALL threads have terminated