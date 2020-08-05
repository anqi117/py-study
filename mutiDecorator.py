def addMother(fn):
	def warp():
		x = fn()
		x.append("Mom-2")
		return x
	return warp

def addFather(fn):
	def warp():
		x = fn()
		x.append("Dad-1")
		return x 
	return warp

@addMother
@addFather
def family():
	x = ["child-0"]
	return x 

r = family()
print(r)
