def job1():
	while True:
		print("---do job1---")
		yield None #generator return None

def job2():
	while True:
		print("---do job2---")
		yield None # generator return None

j1 = job1()
j2 = job2()
while True:
	j1.__next__()
	j2.__next__()
