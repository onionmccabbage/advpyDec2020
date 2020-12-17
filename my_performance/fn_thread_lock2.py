import threading
import time
import random

counter = 0
lock = threading.Lock()
def workerA():
    global counter
    lock.acquire()
    try:
        while counter < 10:
            counter += 1
            print("Worker A is incrementing counter to {}".format(counter))
            sleepTime = random.randint(0,1)
            time.sleep(sleepTime)
    finally:
        lock.release()

def workerB():
    global counter
    lock.acquire()
    try:
        while counter > -10:
            counter -= 1
            print("Worker B is decrementing counter to {}".format(counter))
            sleepTime = random.randint(0,1)
            time.sleep(sleepTime)
    finally:
        lock.release()

def main():
    t0 = time.time()
    thread1 = threading.Thread(target=workerA)
    thread2 = threading.Thread(target=workerB)
    thread2.start() # it matters which thread starts first
    thread1.start()
    thread1.join()
    thread2.join()
    t1 = time.time()
    print("Execution Time {}".format(t1-t0))

if __name__ == '__main__':
    main()