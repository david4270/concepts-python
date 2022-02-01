# Multiprocessing

import os
import threading
import multiprocessing

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

def sqrQueue(mylist, q):
    for num in mylist:
        q.put(num*num)

def printQueue(q):
    print("Queue elements:")
    while not q.empty():
        print(q.get())
    print("Queue is now empty!")

def main():
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

    #reuse mylist = [1,2,3,4,5]
    q = multiprocessing.Queue()

    p6 = multiprocessing.Process(target = sqrQueue, args = (mylist,q))
    p7 = multiprocessing.Process(target = printQueue, args = (q,))

    p6.start()
    p7.start()

    p6.join()
    p7.join()


    print("\nMultiprocessing example 5 - communication between processes: pipe \n")



    #Synchronization and Pooling of processes in Python
    #https://www.geeksforgeeks.org/synchronization-pooling-processes-python/
    print("\nMultiprocessing example 6 - race \n")


    print("\nMultiprocessing example 7 - using locks \n")


    print("\nMultiprocessing example 8 - pooling between processes \n")



if __name__ == "__main__":
    main()