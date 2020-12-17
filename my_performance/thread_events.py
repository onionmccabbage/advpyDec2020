from threading import Thread, Event
import time

class MyClass:
    def __call__(self, name):
        global event
        print( f'{name}: waiting for event...')

if __name__ == "__main__":
    event = Event() # declare an event instance in the global namespace
    m1 = MyClass()
    m2 = MyClass()
    m3 = MyClass()

    t1 = Thread(target=m1, args=('A', ))
    t2 = Thread(target=m1, args=('B', ))
    t3 = Thread(target=m1, args=('C', ))

    t1.start()
    t2.start()
    t3.start()

    time.sleep(5)
    event.set()# here the global event instance gets set, so the thread will have what it is waiting for
    print('all done')