# tcp client socket send data
import struct
from socket import *

clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect(("192.168.3.7", 8899))

sendData = struct.pack("!H", 123)
clientSocket.send(sendData)

reviceData = clientSocket.recv(1024)

print("recvData: %s"%recvData)

clientSocket.close()
