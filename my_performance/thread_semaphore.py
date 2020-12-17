from threading import Thread, Event, Lock, BoundedSemaphore
import time

class DemoSem:
    def __call__(self, name):
        self.name = name
        global sem
        sem.acquire()
        time.sleep(2)
        sem.release()
        print(f'{self.name} done')

if __name__ == "__main__":
    # we need a global semaphore instance
    sem = BoundedSemaphore(3) # this semaphore eill allow up to three threads at a time
    dX = DemoSem()
    dY = DemoSem()
    dZ = DemoSem()
    dA = DemoSem()
    dB = DemoSem()

    tA = Thread(target=dA, args=('A'))
    tB = Thread(target=dB, args=('B'))
    tX = Thread(target=dX, args=('X'))
    tY = Thread(target=dY, args=('Y'))
    tZ = Thread(target=dZ, args=('Z'))

    tA.start()
    tB.start()
    tX.start()
    tY.start()
    tZ.start()

    tA.join()
    tB.join()
    tX.join()
    tY.join()
    tZ.join()

    print('all done')
