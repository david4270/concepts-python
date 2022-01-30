# Multithreading

import os
import threading

#Global variables
x = 0

def incrementCtr():
    global x
    x += 1

def thread_task(lock):
    for _ in range(15):
        print("thread_task assigned to thread {}".format(threading.current_thread().name))
        print("ID of process running thread_task: {}".format(os.getpid()))
        lock.acquire()
        incrementCtr()
        lock.release()

def print_cube(num):
    print("Cube: {}".format(num * num * num))
    print("print_cube assigned to thread {}".format(threading.current_thread().name))
    print("ID of process running print_cube: {}".format(os.getpid()))

def print_sqr(num):
    print("Square: {}".format(num*num))
    print("print_sqr assigned to thread {}".format(threading.current_thread().name))
    print("ID of process running print_sqr: {}".format(os.getpid()))

def main():
    #Multithreading - introduction
    #https://www.geeksforgeeks.org/multithreading-python-set-1/?ref=lbp
    print("\nMultithreading example 1 \n")

    print("main running in thread {}".format(threading.current_thread().name))
    print("ID of process running main: {}".format(os.getpid()))

    t1 = threading.Thread(target = print_sqr, name = 't1', args=(10,))
    t2 = threading.Thread(target = print_cube, name = 't2', args=(10,))

    #Start thread 1
    t1.start()
    #Start thread 2
    t2.start()

    #Wait until thread 1 is completely executed
    t1.join()
    #Wait until thread 2 is completely executed
    t2.join()

    print(t1.is_alive())
    print(t2.is_alive())

    #Multithreading - synchronization
    #https://www.geeksforgeeks.org/multithreading-in-python-set-2-synchronization/
    print("\nMultithreading example 2 \n")

    global x
    x=0

    lock = threading.Lock()

    t3 = threading.Thread(target = thread_task, name = 't3', args=(lock,))
    t4 = threading.Thread(target = thread_task, name = 't4', args=(lock,))

    t3.start()
    t4.start()

    t3.join()
    t4.join()

    # Thread 3    (Request -> Acquire lock)   (Read)  (Increment)  (Write)   (Release Lock)           
    # Thread 4       (Request -> Fail)                                                         (Request -> Acquire Lock)   (Read)  (Increment)  (Write)   (Release Lock)

    for i in range(10):
        print("Iteration {0}: x = {1}".format(i,x))

    print(t3.is_alive())
    print(t4.is_alive())

if __name__ == "__main__":
    main()