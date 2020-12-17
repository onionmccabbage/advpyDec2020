import multiprocessing
import time
def daemonProcess():
    print("Starting my Daemon Process")
    print("Daemon process started:{}".format(multiprocessing.current_process()))
    time.sleep(3)
    print("Daemon process terminating")
    print("Main process: {}".format(multiprocessing.current_process()))

if __name__ == '__main__':
    myProcess = multiprocessing.Process(target=daemonProcess)
    myProcess.daemon = True
    myProcess.start()
    print("We can carry on as per usual and our daemon will continue to execute")
    time.sleep(11)