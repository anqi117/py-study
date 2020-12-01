import struct
from socket import *
import os

# 实现 从服务器下载文件

def main():
	downloadFileName = input("Please input file's name: ")
	# 创建套接字 
	udpSocket = socket(AF_INET, SOCK_DGRAM)
	# 请求命令
	request_cmd = struct.pack("!H%dsb5sb"%len(downloadFileName), 1, downloadFileName, 0, "octet", 0)
	# 发送请求
	udpSocket.sendto(request_cmd, ("192.168.1.10", 69))

	flag = True # 当不能下载的时候，删除open的文件

	f = open(downloadFileName, 'w')

	# 接收服务器的response
	while True:
		reciveData, serverInfo = udpSocket.recvfrom(1024)
		
		operateCode = struct.unpack("!H", reciveData[:2])
		fileBlockNum = struct.unpack("!H", reciveData[2:4])
		
		# 判断当前已经写出的文件序号
		num = 0

		# 如果接受的操作码是3
		if operateCode[0] == 3:
			num = num + 1
			if num == 65535: # 2bytes == 2^16-1
				num = 0 
			#（1)提取内容，写入文件
			if fileBlockNum[0] == num:
				f.write(reciveData[4:])
				
			# 防止上一次ack没有回复到server，而导致的bug
			num = fileBlackNum[0] 
				
			# (2)发送ACK给服务器（4+数据块序号）
			ack_cmd = struct.pack("!HH", 4, fileBlockNum[0])
			udpSocket.sendto(ack_cmd, serverInfo)

		# 如果接受的操作码是5, 指定文件不存在
		elif operateCode[0] == 5:
			print("Specified file %s not found."%downloadFileName)
			flag = False
			break
		
		# 如果接收到的数据长度小于516，break，文件关闭 
		if len(reciveData)<516:
				break

	if flag:
		f.close()
	else:
		os.unlink(downloadFileName)	

if __name__ == '__main__':
	main()