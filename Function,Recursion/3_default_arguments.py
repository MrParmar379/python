#in fucntion when the argument is not given we use default agrument as parameter we want that when we run programer default argument is shown if the argument is not given
def goodDay(name, end="thanks"): # function with  default argument
    print("Good day," + name)
    print(end)

goodDay("Bhavesh","thank you")
goodDay("Mrparmar")
goodDay("Raj", "thank you")