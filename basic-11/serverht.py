#Socket programming with multi-threading
#https://www.geeksforgeeks.org/socket-programming-multi-threading-python/?ref=lbp

import socket
from _thread import *
import threading
import random

print_lock = threading.Lock()

def threaded(c):
    while True:
        
        # data received by client
        data = c.recv(1024)

        if not data:
            print("Bye")

            #lock released on exit
            print_lock.release()
            break
        
        # reverse the given string from client
        if(random.choice([1,2,3,4]) %2 == 0):
            data = data[::-1]
        else:
            #not inverse data
            ()
        
        # send back reversed string to client
        c.send(data)
    
    # close connection
    c.close()

def main():
    host = ""

    # set up port
    port = 12345
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((host,port))

    #put socket in listening mode
    s.listen(5)
    print("socket is listening")

    #loop until client wants to exit
    while True:
        
        # establish connection with client
        c, addr = s.accept()

        #lock acquired by client
        print_lock.acquire()
        print("Connected to:", addr[0], ':', addr[1])

        start_new_thread(threaded,(c,))
    
    s.close()

if __name__ == '__main__':
    main()