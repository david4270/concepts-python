# File handling, OS module, multiprocessing and multithreading, socket

from concurrent.futures import thread
import os
import threading
import multiprocessing

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

def sqrList(mylist, result, square_sum):
    #result array given value
    for idx, num in enumerate(mylist):
        result[idx] = num*num
    #square_sum given value
    square_sum.value = sum(result)
    print("Result in process p3: {}".format(result[:]))
    print("Sum of squares in process p3: {}".format(square_sum.value))

def printRecord(records):
    for rcd in records:
        print("Name: {0} Score: {1}\n".format(rcd[0],rcd[1]))

def insertRecord(rcd, records):
    records.append(rcd)
    print("New record {} added!\n".format(rcd[0]))

def main():
    print("\nos example \n")
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

    #Multiprocessing - introduction
    #https://www.geeksforgeeks.org/multiprocessing-python-set-1/?ref=lbp 
    print("\nMultiprocessing example 1 \n")

    print("ID of main process: {}".format(os.getpid()))

    p1 = multiprocessing.Process(target = print_cube, name = 'p1', args=(10,))
    p2 = multiprocessing.Process(target = print_sqr, name = 'p2', args=(10,))

    p1.start()
    p2.start()

    print("ID of process p1: {}".format(p1.pid))
    print("ID of process p2: {}".format(p2.pid))

    p1.join()
    p2.join()

    print("Process p1 alive: {}".format(p1.is_alive()))
    print("Process p2 alive: {}".format(p2.is_alive()))


    #Multiprocessing - communication between processes
    #https://www.geeksforgeeks.org/multiprocessing-python-set-2/?ref=lbp 
    # Newly created process will 1) run independently and 2) have their own memory space

    print("\nMultiprocessing example 2 - sharing data between processes: shared memory \n")
    # process p3 and main shares shared memory space, which stores result and square_sum

    mylist = [1,2,3,4,5]

    #create array of int data type with space for 5 integers
    result =  multiprocessing.Array('i',5)

    #create value of int type -> can be given initial value
    square_sum = multiprocessing.Value('i')

    # Pass result and square_sum as arguments while creating Process
    p3 = multiprocessing.Process(target = sqrList, args = (mylist,result,square_sum))

    p3.start()
    p3.join()

    print("Result in main process: {}".format(result[:]))
    print("Sum of squares in main process: {}".format(square_sum.value))
    
    print("\nMultiprocessing example 3 - sharing data between processes: server process \n")

    with multiprocessing.Manager() as manager:
        #Create list in server process memory
        records = manager.list( [('Sam',10), ('Adam', 9), ('Kevin', 8)] )
        new_record = ('David', 10)

        p4 = multiprocessing.Process(target = insertRecord, args = (new_record, records))
        p5 = multiprocessing.Process(target = printRecord, args = (records,))
        #Process 4 - join records
        p4.start()
        p4.join()
        #Process 5 - print records
        p5.start()
        p5.join()

    print("\nMultiprocessing example 4 - communication between processes: queue \n")



    print("\nMultiprocessing example 5 - communication between processes: pipe \n")



    #Synchronization and Pooling of processes in Python
    #https://www.geeksforgeeks.org/synchronization-pooling-processes-python/


    #Socket programming
    #
    

    #Socket programming with multi-threading
    #



if __name__ == "__main__":
    main()