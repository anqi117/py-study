from threading import Thread, Lock
from time import sleep


class T1(Thread):
	def run(self):
		while True:
			if lock1.acquire():
				print("---task1---")
				sleep(0.5)
				lock2.release()

class T2(Thread):
	def run(self):
		while True:
			if lock2.acquire():
				print("---task2---")
				sleep(0.5)
				lock3.release()

class T3(Thread):
	def run(self):
		while True:
			if lock3.acquire():
				print("---task3---")
				sleep(0.5)
				lock1.release()

lock1 = Lock()

# 生成锁2， 并且上锁
lock2 = Lock()
lock2.acquire()

# 生成锁3， 并且上锁
lock3 = Lock()
lock3.acquire()


t1 = T1()
t2 = T2()
t3 = T3()

t1.start()
t2.start()
t3.start()

