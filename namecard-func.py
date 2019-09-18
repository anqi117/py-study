card_infor = []
def print_menu():
	print("="*50)
	print(" 名片系统 v1.0")
	print("1. add a new card")
	print("2. delete a card")
	print("3. update a card")
	print("4. search a card")
	print("5. show all of cards")
	print("6. exit")
	print("="*50)

def add_new_card_info():
	new_name = input("name: ")	
	new_qq = input("qq: ")	
	new_wechat = input("wechat: ")	
	new_addr = input("addr: ")

	new_infor = {}
	new_infor['name'] = new_name
	new_infor['qq'] = new_qq
	new_infor['wechat'] = new_wechat
	new_infor['addr'] = new_addr

	# 将一个字典添加到列表中
	global card_infor
	card_infor.append(new_infor)

	print(card_infor)

def delete_card():
	flag = 0
	target_card_name = input("please input the name you want to delete:")
	for i, card in enumerate(card_infor):
		if card['name'] == target_card_name:
			del card_infor[i]
			print(card_infor)
			flag = 1
	if flag == 0:
		print("Card can not be found")

def update_card_info():
	flag = 0
	target_card_name = input("please input the name you want to update:")
	for card in card_infor:
		if card['name'] == target_card_name:
			card['qq'] = input("please input a new qq: ")
			card['wechat'] = input("please input a new wechat: ")
			card['addr'] = input("please input a new addr: ")
			flag = 1
			print("update successd!\n")
			print("%s\t%s\t%s\t%s"%(card['name'], card['qq'], card['wechat'], card['addr']))
			break
	if flag == 0:
			print("Card can not be found.")

def search_card():
	"""search a card by name"""
	search_name = input("name: ")
	global card_infor
	for card in card_infor:
		if card['name'] == search_name:
			print(card)
			break
	else:
		print("There is not a data about %s."%search_name)

def show_all_card():
	print("%s\t%s\t%s\t%s"%("name", "qq", "wechat", "addr"))
	global card_infor
	for card in card_infor:
		print("%s\t%s\t%s\t%s"%(card['name'],card['qq'],card['wechat'],card['addr']))

def main():
	#1 打印功能提示
	print_menu()
	
	while True:
		#2 获取用户输入
		num = int(input("Please input a function number: "))
		#3 根据用户的数据执行相对应的功能
		if num==1:
			add_new_card_info()	
		elif num==2:
			delete_card()
		elif num==3:
			update_card_info()
		elif num==4:
			search_card()
		elif num==5:
			show_all_card()
		elif num==6:
			break
		else:
			print("Please input correct number.")
		
		print("")

main()
