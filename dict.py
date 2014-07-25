# more about dictionaries
# key / value pair
# Dictionaries are unordered

fruits = {"1" : "apples", "2" : "oranges", "3" : "figs", "4" : "bananas", "tropical" : "watermelon"}
print("What fruits are in fridge?", fruits)
print("What fruits is in aisle 2?", fruits["2"])
print("Any tropical fruit in the fridge?", fruits["tropical"])
print("What tropical fruits are in fridge?", "tropical" in fruits) #looks for key
copyitems = fruits.copy()
print("Clear the fridge", fruits.clear(), fruits)
print("What fruits are in fridge?", copyitems)


