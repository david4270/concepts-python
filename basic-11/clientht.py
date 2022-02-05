#Socket programming with multi-threading
#https://www.geeksforgeeks.org/socket-programming-multi-threading-python/?ref=lbp

import socket

def main():
    # local host IP 127.0.0.1
    host = '127.0.0.1'

    port = 12345

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    #connect to server
    s.connect((host,port))

    msg = "Come on you Spurs!"

    while True:
        # send mesage to server
        s.send(msg.encode('ascii'))

        # message received from server
        data = s.recv(1024)

        # print received message
        print("Received from server:",str(data.decode('ascii')))

        #ask client whether to continue
        ans = input("Do you want to continue? (Y/n): ")
        if  ans == "Y" or ans == "y":
            continue
        else:
            break

    # close connection
    s.close

if __name__ == '__main__':
    main()