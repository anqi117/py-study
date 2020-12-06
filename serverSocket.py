# server recive data by tcp

from socket import *

# create server socket
serverSocket = socket(AF_INET, SOCK_STREAM)

# bind
serverSocket.bind(("", 8899))

# turn to listen socket
serverSocket.listen(5)

# accept
clientSocket, clientInfo = serverSocket.accept()

recvData = clientSocket.recv(1024)

print("%s, %s"%(str(clientInfo), recvData)) 

# close
clientSocket.close()
serverSocket.close()
