# list

data = [21,32,23]
print("original data:", data)

# lets append something on the list

data.append(35)
print("calling append with 35:", data)

words = ['Good', 'Bad', 'Ugly', 'Good']
print("Original words are: ", words)

# count number of times a specific word appears in a list
# count is a method defined in list data structure

print("How many time word, Good?: ", words.count("Good"))
print("How many time word, Excellent?: ", words.count("Excellent"))

morewords = ['Excellent', 'Marvellous'] #new list
print("After extend, word list is:", words.extend(morewords), words)  #extend the list
print("How many time word, Excellent?: ", words.count("Excellent"))

# lets create a list of Fruits and discover more methods or functions

fruits = ['apple', 'banana', 'strawberry', 'oranges']
print("My list of fruits is", fruits)
print("Where is the index of strawberry?", fruits.index("strawberry"))
print("lets insert something after banana", fruits.insert(3,"figs"), fruits)
print("lets reverse my list of fruits", fruits.reverse(), fruits)
print("lets sort my list of fruits", fruits.sort(), fruits)

fruitstuple = ("apple","banana","oranges")
#fruitstuple.insert("figs")
