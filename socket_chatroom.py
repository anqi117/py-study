from socket import *

def main():
		udpSocket = socket(AF_INET, SOCK_DGRAM)

		udpSocket.bind(("", 7788))

		while True:
			recvData = udpSocket.recvfrom(1024)
			print("[%s]:%s"%(str(recvData[1]), recvData[0].decode("gb2312"))


if __name__ == "__main__":
		main()
