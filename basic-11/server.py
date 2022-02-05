import socket

#Socket programming
#https://www.geeksforgeeks.org/socket-programming-python/?ref=lbp 

def server():
    #create socket object
    s = socket.socket()

    #set port to communicate
    port = 12345

    #bind the port
    #no IP input, this makes server listen to requests
    s.bind(('', port))
    print("Socket binded to %s" %(port))

    #put socket into listening mode
    s.listen(5)
    print("Socket is listening")

    # Unless break happens or error occurs, this runs forever
    while True:
        #Establish connection with client
        c, addr = s.accept()
        print("Got connection from", addr)

        #send thank you message to client, encode to send byte type
        c.send("Thank you for connecting".encode())

        #close connection with client
        c.close()
        break

server()