def fribonacci(num):
	if num > 1:
		return num * fribonacci(num-1)
	else:
		return num


result=fribonacci(5)
print(result)
