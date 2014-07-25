# list is basic storage in Python and it automatically numbers your list and first element starts with '0'
# A list is within []

#starts from zero
# or, backwards from -1
family = ['mom', 'dad', 'bro', 'sis', 'cat']

print(family[0])
print(family[1])
print(family[2])
print(family[3])
print(family[4])

print()
print(family[-1])
print(family[-2])
print(family[-3])
print(family[-4])
print(family[-5])

#you can slice information in a list
print()
print("Printing sliced info:", family[2:5])
print("Printing sliced info:", family[0:])
print("Printing sliced info:", family[:5])
print("Printing sliced info:", family[:1])
print("Printing sliced info:", family[2:50])
print("Printing sliced info:", family[:])

# string characters can also be accessed by simply pointing to location starting from zero
print()
print('python'[0], 'python'[1], 'python'[4])

