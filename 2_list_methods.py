#METHODS OF LIST
# LI .sort(): updates the list to [1 ,2,7,8, 15,21 |
# LI .reverse(): updates the list to (15,21 ,2,7,8,1]
# LI .append(8): adds 8 at the end the list
# LI .insert(3,8): This wilt add 8 at 3 index
# LI .pop(2): Will delete element at index 2 and return its value.
# LI .remove(21): Will remove 21 from the list.

# Add methiods = append,extend,insert
# delete = clear,remove,pop


friends = ["Apple", "Orange" ,5,345.06,False,"Aakash", " Rohan", 3,3,3]
# print(friends)


# append method add the element  at the end of the list
friends. append( "Bhavesh " )
print (friends)

#extend(iterable) method is used to add new list items to the existing list
friends.extend([34,"Raj"])
print(friends)

friends.pop() # remove the last element in the list
friends.pop(2) #remove element as a index number
print(friends)

# for using index and count method we have to declare one more ans variable to perform the function
Ans1=friends.count(3) #Returns the number of times 3 appears in the list.
print(Ans1)
Ans=friends.index("Orange")
print(Ans)

list1 = friends.copy() # copy method is used to copy the list 
print(list1)

# EXPLANATION 1:
l1= [1, 34,62, 2, 6, 11]
l1.sort() # sort the list ascending order 
print(l1)

l1= [1, 34,62, 2, 6, 11]
l1.reverse() # reverse the list
print(l1)

l1.insert(2, 333333) # Insert 333333 such that its index in the list is 
print(l1)

l1= [1, 34,62, 2, 6, 11]
l1.pop(3) # delete the element by 
print(l1)

l1.remove(34) #Removes the first occurrence of item x from the list.
print(l1)

# EXPLANATION 2:
l1= [1, 34,62, 2, 6, 11]

l1.sort() # sort the list ascending order 
l1.sort(reverse=True) # sorted in reverse form
l1.insert(2, 333333) # Insert 333333 such that its index in the list is
l1.remove(34)
# l1.clear() delete whole list
print(l1)