str1 ="Bhavesh is learning python"

#open function use two parameter filname and mode(read and write) read is bydefault avaiilable in oprn function and for write function we write"w" as parameter after writing file name 
f = open("myfile.txt","w")
f.write(str1)
f.close()