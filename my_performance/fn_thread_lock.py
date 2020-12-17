from threading import Lock
import sys
import random
import time

# create a thread lock
lock = Lock()
# acquire the lock
lock.acquire()
try:
    for i in range(1,50):
        sys.stdout.write(f'{i}')

finally:
    # always make sure to release the lock
    lock.release()

# or use with
with lock:
    for i in range(1,50):
        sys.stdout.write(f'{i}')
    # the lock is autamically released when with ends