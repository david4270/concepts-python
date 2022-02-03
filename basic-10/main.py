# Multiprocessing

import os
import threading
import multiprocessing

############### Example 1 ##################

def print_cube(num):
    print("Cube: {}".format(num * num * num))
    print("print_cube assigned to thread {}".format(threading.current_thread().name))
    print("ID of process running print_cube: {}".format(os.getpid()))

def print_sqr(num):
    print("Square: {}".format(num*num))
    print("print_sqr assigned to thread {}".format(threading.current_thread().name))
    print("ID of process running print_sqr: {}".format(os.getpid()))

############# Example 2 ######################

def sqrList(mylist, result, square_sum):
    #result array given value
    for idx, num in enumerate(mylist):
        result[idx] = num*num
    #square_sum given value
    square_sum.value = sum(result)
    print("ID of process running sqrList: {}".format(os.getpid()))
    print("Result in process p3: {}".format(result[:]))
    print("Sum of squares in process p3: {}".format(square_sum.value))

############# Example 3 ######################

def printRecord(records):
    print("ID of process running printRecord: {}".format(os.getpid()))
    for rcd in records:
        print("Name: {0} Score: {1}\n".format(rcd[0],rcd[1]))

def insertRecord(rcd, records):
    print("ID of process running insertRecord: {}".format(os.getpid()))
    records.append(rcd)
    print("New record {} added!\n".format(rcd[0]))

############# Example 4 ######################

def sqrQueue(mylist, q):
    print("ID of process running setQueue: {}".format(os.getpid()))
    for num in mylist:
        q.put(num*num)

def printQueue(q):
    print("ID of process running printQueue: {}".format(os.getpid()))
    print("Queue elements:")
    while not q.empty():
        print(q.get())
    print("Queue is now empty!")

############# Example 5 ######################

def sender(conn,msgs):
    print("ID of process running sender: {}".format(os.getpid()))
    for m in msgs:
        #use send() method to send message from one end of pipe
        conn.send(m)
        print("Send the message:",m)
    conn.close()

def receiver(conn):
    print("ID of process running receiver: {}".format(os.getpid()))
    while 1:
        #use recv() method to receive message at the other end of pipe
        msg = conn.recv()
        if msg == "END":
            break
        print("Received the message:",msg)


############# Example 6 ######################

# Withdraw from account
def withdraw(balance):
    print("ID of process running withdraw: {}".format(os.getpid()))
    for _ in range(10000):
        balance.value = balance.value - 1

# Deposit to account
def deposit(balance):
    print("ID of process running deposit: {}".format(os.getpid()))
    for _ in range(10000):
        balance.value = balance.value +1

# Perform transactions
def perform_transactions():
    #initial balance
    balance = multiprocessing.Value('i',100)

    pA = multiprocessing.Process(target = withdraw, args=(balance,))
    pB = multiprocessing.Process(target = deposit, args=(balance,))

    pA.start()
    pB.start()

    pA.join()
    pB.join()

    print("Final Balance:",balance.value)

############# Example 7 ######################

# Withdraw from account
def withdraw_withLock(balance, lock):
    print("ID of process running withdraw: {}".format(os.getpid()))
    for _ in range(10000):
        lock.acquire()
        balance.value = balance.value - 1
        lock.release()

# Deposit to account
def deposit_withLock(balance, lock):
    print("ID of process running deposit: {}".format(os.getpid()))
    for _ in range(10000):
        lock.acquire()
        balance.value = balance.value +1
        lock.release()

# Perform transactions
def perform_transactions_withLock():
    #initial balance
    balance = multiprocessing.Value('i',100)

    lock = multiprocessing.Lock()

    pC = multiprocessing.Process(target = withdraw_withLock, args=(balance,lock))
    pD = multiprocessing.Process(target = deposit_withLock, args=(balance,lock))

    pC.start()
    pD.start()

    pC.join()
    pD.join()

    print("Final Balance:",balance.value)

############# Example 8 ######################



################## main ######################

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
    #Create multiprocessing queue
    q = multiprocessing.Queue()

    #in sqrQueue, insert into queue
    p6 = multiprocessing.Process(target = sqrQueue, args = (mylist,q))
    #in printQueue, get queue content
    p7 = multiprocessing.Process(target = printQueue, args = (q,))

    p6.start()
    p7.start()

    p6.join()
    p7.join()


    print("\nMultiprocessing example 5 - communication between processes: pipe \n")

    msgList = ["Tottenham","are","the","greatest","team","that","the","world","has","ever","seen","END"]

    #Create pipe
    parCon, chiCon = multiprocessing.Pipe()

    p8 = multiprocessing.Process(target = sender, args = (parCon, msgList)) #set sender pipe
    p9 = multiprocessing.Process(target = receiver, args = (chiCon,)) #set receiver pipe

    p8.start()
    p9.start()

    p8.join()
    p9.join()


    #Synchronization and Pooling of processes in Python
    #https://www.geeksforgeeks.org/synchronization-pooling-processes-python/
    print("\nMultiprocessing example 6 - race \n")

    for _ in range(10):
        # perform_transactions() for 10 times
        perform_transactions()
    
    # Oh no! Process racing happens. Expected to have 100 as final balance (100-10000+10000)
    # This happens due to concurrent access of processes to the shared data 'balance' -> race condition

    """
    current balance = 100

    pA    read()                   balance = 100-1 = 99
    pB                read()                                 balance = 100+1 = 101    

    WRONG OPERATION CARRIED OUT!
    """

    """
    current balance = 100

    pA    read()     balance = 100-1 = 99
    pB                                         read()       balance = 99+1 = 100   

    Operation carried out properly
    """

    """
    current balance = 100

    pA                                         read()       balance = 101-1 = 100
    pB    read()     balance = 100+1 = 101    

    Operation carried out properly
    """

    print("\nMultiprocessing example 7 - using locks \n")

    for _ in range(10):
        # perform_transactions_withLock() for 10 times
        perform_transactions_withLock()
    
    # Okay, this one returns proper value (100) lol. Why does it happen?
    # Because withdraw and deposit happens after the lock is acquired!!
    # Making sure that shared data 'balance' is accessed by only one process every time

    """
    current balance = 100

    pA    read()      lock     balance = 100-1 = 99    release
    pB                                                           read()     lock    balance = 99+1 = 100    release
 
    Operation carried out properly
    """

    """
    current balance = 100
 
    pA                                                            read()    lock    balance = 101-1 = 100    releasse
    pB    read()      lock     balance = 100+1 = 101    release  

    Operation carried out properly
    """

    print("\nMultiprocessing example 8 - pooling between processes \n")



if __name__ == "__main__":
    main()