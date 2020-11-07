# 多线程里面的生产者与消费者模式
# 这个模式 主要是为了解决多线程任务的时候，生产方与利用方的速度不匹配问题，导入阻塞队列的概念作为一个缓冲，可以实现上述问题的解耦。

from threading import Thread
from queue import Queue
from time import sleep


class Producer(Thread):
	global qu
	def run(self):
		while True:
			if qu.qsize() < 1000:
				# 生产100个产品
				for i in range(100):
					msg = "生产产品"+str(i)
					print(msg)
					qu.put(msg)
			sleep(1)

class Consumer(Thread):
	global qu
	def run(self):
		while True:
			if qu.qsize() > 100:
				# 消费100个产品
				for i in range(100):
					msg = self.name+"消费了"+qu.get()
					qu.get()
					print(msg)
			sleep(0.5)

if __name__ == "__main__":
	qu = Queue()
	for i in range(500):
		qu.put("初始产品"+str(i))

	for i in range(2):
		p = Producer()
		p.start()

	for i in range(3):
		c = Consumer()
		c.start()
