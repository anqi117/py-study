# 简单的工厂模式
# 通过添加一个类，实现原本的2个类解耦的效果。
# 以下の例の場合、料理の注文と作成をFactoryクラスを追加することで、完全に分離することを実現する。


# 導入前
class Restaurant(object):
	def order(self, meal):
		if meal == "ramen":
			return Ramen()
		elif meal == "sushi":
			return Sushi()
		elif meal == "tenpura":
			return Tenpura()

class Meal():
	def smellGood(self):
		print("semll so goood!!")

class Ramen(Meal):
	pass

class Sushi(Meal):
	pass

class Tenpura(Meal):
	pass

# restaurant実例対象
restaurant1 = Restaurant()
myRamen = restaurant1.order("ramen")
myRamen.smellGood()

# 上の例の場合、料理の種類を増えるとともに、店を管理する人も改修する必要がある。非常に不便、非効率。
# Factory classを導入することで、店の管理者は料理の種類の変更に気にせず管理できる。

# 導入後
class NewRestaurant(object):
	def __init__(self):
		self.Factory = Factory()

	def order(self, meal):
		return self.Factory.select_your_meal(meal)

# ---------上は店管理者管理、下料理長管理---------
class Factory(object):
	def select_your_meal(self, meal):
		if meal == "ramen":
			return Ramen()
		elif meal == "sushi":
			return Sushi()
		elif meal == "tenpura":
			return Tenpura()

restaurant2 = NewRestaurant()
# 料理長が料理を作る
mySushi = restaurant2.order("sushi")
mySushi.smellGood()
