#readlines mode return the lines in file as a list

f = open("myfile.txt")
data = f.readlines()
print(data)
print(data,type(data))
f.close()