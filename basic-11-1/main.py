import socket, ssl
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import time

def main():
    
    # HTTP(S) Socket
    print("HTTP(S) socket Example")
    HOST = "www.youtube.com"
    PORT = 443

    context = ssl.SSLContext(ssl.PROTOCOL_TLSv1)
    m = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    mysock = context.wrap_socket(m, server_hostname= HOST) 
    mysock.connect((HOST, PORT))
    cmd = "GET / HTTP/1.1\r\nHost: www.youtube.com\r\n\r\n".encode()
    mysock.send(cmd)

    ctr = 0
    while ctr < 10: #there are so many things to print, so decided to cap instead
        data = mysock.recv(512).rstrip()
        if(len(data) < 1):
            break
        time.sleep(0.2)
        print(data.decode())
        ctr += 1
    
    mysock.close()

    #URLLIB Example
    print("")
    print("URLLIB Example")
    fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
    # HTTPS is more complicated, similar to above approach
    
    counts = dict()
    for line in fhand:
        words = line.decode().split()
        print(line.decode().strip())
        time.sleep(0.2)
        for word in words:
            counts[word] = counts.get(word,0) + 1
    
    print(counts)

    # BeautifulSoup example
    # If BeautifulSoup is not installed, please install using the following line:
    # pip install beautifulsoup4
    # https://www.geeksforgeeks.org/beautifulsoup-installation-python/
    
    print("")
    print("BeautifulSoup Example")

    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE

    url = input('Enter URL: ')
    html = urllib.request.urlopen(url, context = ctx).read()
    soup = BeautifulSoup(html, 'html.parser')

    # Retrieve all of anchor tags
    tags = soup('a')

    for tag in tags:
        print(tag.get('href', None))





if __name__ == '__main__':
    main()