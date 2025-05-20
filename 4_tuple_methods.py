#METHODS OD TUPLE
my_tup = (1,4,"Bhavesh","Raj",67.4, 78,34)
print(my_tup)

# Returns the length (number of elements) of the tuple.
print(len(my_tup))  

# return maximum value
my_tup = (1,4,67.4, 78,34) 
print(max(my_tup))

# return minimum value
my_tup = (1,67.4, 78,34)
print(min(my_tup))

#return sum of all the numbers in tuple
my_tup = (1,4,67.4, 78,34)
print(sum(my_tup))

# return if any of the value is given in tuple
my_tup = (1,4,"Bhavesh","Raj",67.4, 78,34)
print(any(my_tup))

# return if all the values are in tuple
my_tup = (1,4,"Bhavsh","Parmar",67.4, 78,34)
print(all(my_tup))

# sort the value in ascending order
# there are two methods sort will sort the original tuple and sorted will give the new sorted tuple
my_tup = (1,4,67.4, 78,34)
ans = sorted(my_tup)
print(ans)

# convert list into tuple
my_list = (1,4,"Bhavsh","Parmar",67.4, 78,34)
ans = tuple(my_tup)
print(ans)

# count the perticular value in tuple
my_tup = (1,4,"Bhavsh","Parmar",67.4, 78, 4)
ans = my_tup.count(4)
print(ans)

# give the index value of number
my_tup = (1,4,"Bhavsh","Parmar",67.4, 78, 4)
ans = my_tup.index(4)
print(ans)


# Concatenation: Tuples can be concatenated using the operator.
tuplel = (1,2,3)
tuple2 = (4, 5, 6)
concatenated = tuplel + tuple2
print(concatenated)

# unpacking: Tuples can be unpacked into individual variables.
my_tuple = (1,2,3,)
a, b, c = my_tuple
print(a, b, c)

# Slicing: Tuples support slicing to create a new tuple from a subset of the original.
my_tuple = (1,2,3,4,5)
sliced = my_tuple[1:4]
print (sliced)

# Membership: You can check if an item exists in a tuple using the keyword.
my_tup = (1,2,3,4,5)
print(2 in my_tup)
print(5 in my_tup)


