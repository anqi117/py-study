def func_arg(arg="hello"):
	def func(fn):
		def func_in():
			print("The annotation's argument is %s"%arg)
			fn()
		return func_in
	return func

@func_arg("10000.blog")
def test():
	print("-----test-----")

test()
