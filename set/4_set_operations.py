my_set = {1,3,5,7,9}
my_set1 = {2,4,6,8,10}
print("Original set:", my_set)

# union: Returns a new set with elements from the set and all others.
print(my_set.union(my_set1))

# intersection: Returns a new set with elements common to the set and all others.
print(my_set.intersection(my_set1))

# difference: Returns a new set with elements in the set that are not in the others.
print(my_set.difference(my_set1))

# symmetric_difference(other)
# Returns a new set with elements in either the set or the other set, but not both.
print(my_set.symmetric_difference(my_set1))

# membership testing: it return the result as true or false as a boolean value
# issubset:Checks if the set is a subset of another set.
print(my_set.issubset(my_set1))

# issuperset:Checks if the set is a superset of another set.
print(my_set.issuperset(my_set1))

# isdisjoint(other): Checks if the set has no elements in common with another set.
print(my_set.isdisjoint(my_set1))