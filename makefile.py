f = open("1.py", "w")
f.write("test123")
f.close()

f = open("1.py", "r")
content = f.read()
f.close()

x = open("2.py", "w")
x.write(content)
x.close()
