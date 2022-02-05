import socket

#Socket programming
#https://www.geeksforgeeks.org/socket-programming-python/?ref=lbp 

def client():

    # Create a socket object
    s = socket.socket()

    #Define a port to connect
    port = 12345

    #connect to local computer
    s.connect(('127.0.0.1',port))

    # Receive data from the server and decoding to get the string
    print(s.recv(1024).decode())
    
    # Close the connection
    s.close()

client()