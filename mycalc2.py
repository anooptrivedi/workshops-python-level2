# An intermediate calculator

# return sum of num1 and num 2
def add(num1, num2): #function signature with 2 arguments
    return num1 + num2

# return subtraction of num1 and num 2
def sub(num1, num2):
    return num1 - num2

# return multiplication of num1 and num 2
def mult(num1, num2):
    return num1 * num2

# return division of num1 and num 2
def div(num1, num2):
    return num1 / num2

# return exponential of num1 and num2
def exp(num1, num2):
    return num1**num2 #you can also use inbuilt function pow(num1, num2)

# return remainder of num1 and num2
def rem(num1, num2):
    return num1%num2

# think about abs, sqrt, floor (import math module first) - e.g to use math.sqrt(num1)

def main():
    operations = input("What do you want to do? (+, -, *, /,**,%): ")
    if(operations != '+' and operations != '-' and operations != '*' and operations != '/' and operations != '**' and operations != '%'):
        print('You must enter a valid opertions')
    else:
        num1 = int(input('Enter First Number: ')) #cast to integer from a string
        num2 = int(input('Enter Second Number: '))
        if(operations == '+'):
            print(add(num1, num2))
        elif(operations == '-'):
            print(sub(num1, num2))
        elif(operations == '/'):
            print(div(num1, num2))
        elif(operations == '**'):
            print(exp(num1, num2))
        elif(operations == '%'):
            print(rem(num1, num2))
        else:
            print(mult(num1, num2))

#calling the main function
main()
