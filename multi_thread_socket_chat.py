from threading import Thread
from socket import *

def recvData():
	while True:
		recvInfo = udpSocket.recvfrom(1024)
		print("\r>>%s:%s"%(str(recvInfo[1]), recvInfo[0].decode("utf-8")))
		print(">>")

def sendData():
	while True:
		sendInfo = input("<<")
		udpSocket.sendto(sendInfo.encode("utf-8"), (destIp, destPort))

udpSocket = None
destIp = ""
destPort = 0

def main():
	global udpSocket
	global destIp
	global destPort

	udpSocket = socket(AF_INET, SOCK_DGRAM)
	udpSocket.bind(("", 7788))
	
	destIp = input("input destination IP: ")
	destPort = int(input("input destination Port: "))

	tr = Thread(target=recvData)
	ts = Thread(target=sendData)
	
	tr.start()
	ts.start()
	
	tr.join()
	ts.join()

if __name__ == "__main__":
	main()
