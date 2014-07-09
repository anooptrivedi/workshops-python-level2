# A simple calculator

def add(num1, num2): #function signature with 2 arguments
    return num1 + num2 #adding two values

def sub(num1, num2):
    return num1 - num2 #subtracting two argument values

def mult(num1, num2):
    return num1 * num2 #multiplying two argument values

def div(num1, num2):
    return num1 / num2 #dividing two argument values

num1 = 1
num2 = 2

myValues = print("Adding two values: (", num1, num2, '):', add(num1, num2))
myValues = print("Subtracting two values: (", num1, num2, '):', sub(num1, num2))
myValues = print("Multiplying two values: (", num1, num2, '):', mult(num1, num2))
myValues = print("Divide two values: (", num1, num2, '):', div(num1, num2))
