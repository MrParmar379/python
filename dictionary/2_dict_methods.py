marks = {
    "Harry": 100,
    "Shubham": 56,
    "Rohan": 23
}
print("ORIGINAL DICTIONARY:")
print(marks)

#METHODS OF DICT
# ITEM : it will give all the key+values(items) in the form of tuple
print(marks.items())

#KEYS: it will give all the key values we can also say that index value
print(marks.keys())

#VALUES: it will give all the values in the dict
print(marks.values())

# UPDATE: update the existing items in dict also add new key_values in dict
marks.update({"Harry":99, "kritika": 100})
print(marks)

#GET: get method gives the values according to key if it is not present in dict it returns the none 
print(marks.get("prachi"))
print(marks["Harry2"]) # it will generate the KeyError: 'Harry2' 

# CLEAR: Removes all items from the dictionary.
my_dict = {'a': 1, 'b': 2}
my_dict.clear()
print(my_dict)  # Output: {}

# COPY :Returns a shallow copy of the dictionary.
my_dict = {'a': 1, 'b': 2}
new_dict = my_dict.copy()
print(new_dict)  # Output: {'a': 1, 'b': 2}

# FROMKEY: Creates a new dictionary with keys from the given iterable, each initialized to the specified value.
keys = ['a', 'b', 'c']
my_dict = dict.fromkeys(keys, 0)
print(my_dict)  # Output: {'a': 0, 'b': 0, 'c': 0}

# POP :Removes the specified key and returns its value. If the key is not found, returns the default value.
my_dict = {'a': 1, 'b': 2}
value = my_dict.pop('a')
print(value)      # Output: 1
print(my_dict)    # Output: {'b': 2}

# POPITEM:Removes and returns the last inserted key-value pair as a tuple.
my_dict = {'a': 1, 'b': 2}
item = my_dict.popitem()
print(item)       # Output: ('b', 2)
print(my_dict)    # Output: {'a': 1}

# SETDEFAULT:Returns the value of the specified key if it exists; otherwise, inserts the key with the specified default value and returns it.
my_dict = {'a': 1}
value = my_dict.setdefault('b', 2)
print(my_dict)    # Output: {'a': 1, 'b': 2}

