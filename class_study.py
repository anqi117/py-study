class Cat():
	def __init__(self, name, age, left_hp):
		self.name = name
		self.age = age
		self.left_hp = left_hp

	def __str__(self):
		return("class information: name: %s, age: %d"%(self.name, self.age))
	def eat(self, food):
		print("eating..")
		self.left_hp += food.value
		if self.left_hp < 10:
			print("I am famished, deading...")
		elif 10 <= self.left_hp < 80:
			print("I ate %s, but i'm still hangry."%food.name)
		elif self.left_hp >= 80:
			print("I'm full. Thank you for having me. current_hp=%d"%self.left_hp)

	def introduce(self):
		print("My name is %s, %d years old."%(self.name, self.age))

class CatFood():
	def __init__(self, new_name, new_value):
		self.name = new_name
		self.value = new_value

	def __str__(self):
		return("New catfood's name is %s with %d g weight."%(self.name, self.value))

tom = Cat("tom", 30, 0)
tom.introduce()
print(tom)

catfood1 = CatFood("Seven Star cat food", 80)
print(catfood1)
tom.eat(catfood1)
