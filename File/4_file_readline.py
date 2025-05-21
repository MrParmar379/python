# readline mode it ready everytime one line from the file 
f = open("myfile.txt")
# data1 = f.readline()
# print(data1,type(data1))

# data1 = f.readline()
# print(data1,type(data1))

# data2 = f.readline()
# print(data2,type(data2))

# data3 = f.readline()
# print(data3,type(data3))

# data4 = f.readline()
# print(data4,type(data4))

# we are read line by line through loop it makes the program easy
data1 = f.readline()
while data1 != "":
    print(data1)
    data1 = f.readline() 
f.close()

