my_set = {1,3,5,7,9}

#METHODS OF SET
#add : adding the element in the set which can be placed anywhere not compulsory in last place bec set is not indexed
my_set.add( 6)
print(my_set)

# Update: add new element in existing set
my_set.update([8])
print(my_set)

# remove: Removes a specific element from the set. Raises a KeyError if the element is not found.

# my_set.remove(10)
# print(my_set)

#discard: Removes a specific element from the set. Does not raise an error if the element is not found.
my_set.discard(3)
print(my_set)

# pop: Removes and returns an arbitrary element from the set. Raises a KeyError if the set is empty./
my_set.pop()
print(my_set)

# clear: Removes all elements from the set.
my_set.clear()
print(my_set)

