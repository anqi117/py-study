# singleton instance

class Test(object):
	# 定义类属性
	__instance = None

	# 定义实例属性
	__init_flag = False

	# 重写new方法，如果已经生成一个实例，那么不再生成
	# 重新new方法时，需要调用父类的new方法
	def __new__(cls, name):
		if cls.__instance == None:
			cls.__instance = object.__new__(cls)
			return cls.__instance
		else:
			print("already existed, Making new instance failed.")
			return cls.__instance

	def __init__(self, name):
		if self.__init_flag == False:
			print("---init---")
			self.name = name
			self.__init_flag = True

t1 = Test("t111")
print(t1.name)
print(id(t1))

t2 = Test("t222")
print(t2.name)
print(id(t2))
