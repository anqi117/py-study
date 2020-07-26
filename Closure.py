def make_line_equation(x):
	def tell_u_y(givemea, givemeb):
		return givemea*x + givemeb

	return tell_u_y

x = 5
line = make_line_equation(x)
# 给出a, b算出函数的斜率 slope
y = line(1, 1)

print("y is %d, when x=%d by using line."%(y, x))
