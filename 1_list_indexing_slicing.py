# original list
friends = ["Apple", "Orange", 5, 345.06, False, "Aakash", "Rohan"]
print(friends)

# indexsing the list
print(friends[0])
friends[0] = "Grapes" # Unlike Strings lists are mutable
print (friends [0])
print (friends [1])
# print (friends [20]) #error

# slicing the list
print (friends [1:4])
print (friends [-4:-2])
print (friends [:4]) # stars with the 0 index
print (friends [1:])
print (friends [:]) # print whole list

