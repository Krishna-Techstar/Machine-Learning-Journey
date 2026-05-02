f = open("sample1.txt", "r")
data = f.read()
print(data)
print(type(data))

x = open("sample1.txt", "r")
data = x.readline()
print(data)

y = open("sample1.txt", "r")
data = y.readlines()

f.close()