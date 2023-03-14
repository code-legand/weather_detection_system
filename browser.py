from socket import *

mysoc = socket(AF_INET, SOCK_STREAM)
mysoc.connect(('localhost', 8000))
mysoc.sendall('GET / HTTP/1.0\r\n\r\n'.encode())
while True:
    data = mysoc.recv(512)
    if (len(data) < 1):
        break
    print(data.decode())
mysoc.close()
