class Dog(object):
	__instance = None
	# 初期化初回のみ
	__init_flag = False
	
	def __new__(cls, name):
		if cls.__instance == None:
			cls.__instance = object.__new__(cls)
			return cls.__instance
		else:
			# すでに一回newした場合、既存instanceを返す
			return cls.__instance

	def __init__(self, name):
		if Dog.__init_flag == False:
			self.name = name
			Dog.__init_flag = True

a = Dog("dog1")
print(id(a))
print(a.name) # dog1

b = Dog("dog2")
print(id(b))
print(b.name) # dog1

print(id(a))
print(a.name) # dog1
