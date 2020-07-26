def make_line_equation(a, b):
	def tell_u_y(givemex):
		return a*givemex + b

	return tell_u_y

a = 1
b = 1
# 给出a, b算出函数的斜率 slope, 确定函数
line = make_line_equation(a, b)
# 给x求y
x = 5
y = line(x)

print("y=%d, when x=%d by using y=%dx+%d."%(y, x, a, b))
