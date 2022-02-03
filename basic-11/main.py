# Socket programming

import os
import threading
import socket
import sys



def main():
    #Socket programming
    #https://www.geeksforgeeks.org/socket-programming-python/?ref=lbp 
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print("Socket successfully created")
    except socket.error as err:
        print("socket creation failed with error %s" %(err))
    
    port = 80

    try:
        host_ip = socket.gethostbyname('www.google.com')
    except socket.gaierror:
        print("there was an error resolving the host")
        sys.exit()
    
    s.connect((host_ip,port))
    print("the socket has successfully connected to google at {0} port {1}".format(host_ip,str(port)))

    #Socket programming with multi-threading
    #https://www.geeksforgeeks.org/socket-programming-multi-threading-python/?ref=lbp


if __name__ == "__main__":
    main()