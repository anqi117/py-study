class Test(object):
	def __init__(self, func):
		print("The function name is %s"%func.__name__)
		self.__func = func

	def __call__(self):
		print("---通过装饰器执行的功能---")
		self.__func()

@Test
def liu():
	print("---original liu----")


liu()
