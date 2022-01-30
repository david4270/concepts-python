# File handling, OS module, multiprocessing and multithreading, socket

from concurrent.futures import thread
import os
import threading
import time

#Global variable x
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
    #os.getcwd - get current directory
    dir = os.getcwd()
    print(dir)
    
    #os.path.join - joins two strings to make path
    expdir = os.path.join(dir,"example project")

    #os.path.exists - finds if the directory exists
    if(not(os.path.exists(expdir))):
        #os.mkdir - makes directory
        os.mkdir("example project")
    
    #Read/Write file
    # w - write file, r - read file, a - append file
    f = open("example project\demo.txt","w")
    f.write("Glory Glory Tottenham Hotspur\nGlory Glory Tottenham Hotspur\nGlory Glory Tottenham Hotspur\nAnd the Spurs go marching on\n")
    f.close()

    f = open("example project\demo.txt","r")
    t = f.read()
    print(t)
    f.close()

    f = open("example project\demo.txt","a")
    f.write("\nTottenham are the greatest team that the world has ever seen\nTottenham are the greatest team that the world has ever seen\nTottenham are the greatest team that the world has ever seen\nAnd the Spurs go marching on\n")
    f.close()

    f = open("example project\demo.txt","r")
    t = f.read()
    print(t)
    f.close()

    #Another way of file handling
    with open("example project\demo2.txt","w") as f2:
        f2.write("hello\n")
    
    #os.listdir - lists directory
    print(os.listdir(expdir))
    
    #os.path.getsize - gets size
    sz = os.path.getsize(os.path.join(expdir,"demo.txt"))
    print("demo.txt is",sz,"Bytes")

    sz = os.path.getsize(os.path.join(expdir,"demo2.txt"))
    print("demo2.txt is",sz,"Bytes")

    #os.remove - removes file
    os.remove("example project\demo.txt")
    os.remove("example project\demo2.txt")

    if(os.path.exists(expdir)):
        #os.rmdir - removes directory
        os.rmdir("example project")
        print("Removed directory")
    
    #os.name prints name of os - if runs in windows 11, returns 'nt'
    print(os.name)

    #Multithreading - introduction
    #https://www.geeksforgeeks.org/multithreading-python-set-1/?ref=lbp

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

    #Multithreading - synchronization
    #https://www.geeksforgeeks.org/multithreading-in-python-set-2-synchronization/
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

    #Multiprocessing - introduction
    #https://www.geeksforgeeks.org/multiprocessing-python-set-1/?ref=lbp 


    #Multiprocessing - communication between processes
    #


    #Socket programming
    #
    

    #Socket programming with multi-threading
    #



if __name__ == "__main__":
    main()