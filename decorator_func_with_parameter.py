def func(funcName):
	def func_in(*args, **kwargs): # recive the test() func's parameter
		print("Processing in Decorator...")
		res = funcName(*args, **kwargs)
		return res
	return func_in

@func
def test(a, b):
	print("Using a = %s, b = %s in func test."%(a, b))
	return (a, b)

res = test(11, 22)
print(res)
