class Cat():
	# metho
	def __init__(self, name, age):
		self.name = name
		self.age = age

	def __str__(self):
		return("class information: name: %s, age: %d"%(self.name, self.age))
	def eat(self):
		print("eating..")
	
	def introduce(self):
		print("My name is %s, %d years old."%(self.name, self.age))

tom = Cat("tom", 30)
tom.introduce()
print(tom)
