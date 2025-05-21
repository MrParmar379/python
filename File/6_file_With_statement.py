# With statement is the best way to open and close the file automatically
# f = open("file.txt")
# data = f.read()
# print(data)
# f.close()

with open("file.txt") as f:
    print(f.read())