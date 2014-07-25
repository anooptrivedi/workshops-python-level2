"""
A prime number is a natural number greater than 1 that has no positive divisors other
than 1 and itself.

example 2, 3, 5, 7, 11, 13, 17, 19, ...
"""
def isPrime(number):
    min=2 #minimum number to be prime
    flag = True #default flag to find if number is prime

    while (min != number):
        if (number % min == 0): #find if there is remainder
            print("The", number, "is not prime")
            flag = False
            break
        #print(min)
        min += 1

    if (flag == True):
        print(number, "is Prime")


while True:

    number = input('What number do you want to find is a prime? ')

    try:
        number = int(number)
        if(number <= 1):
            print("Goodbye!, less than 2, invalid to check for Prime Number")
            break
        else:
            isPrime(number)
    except ValueError:
        print(number, "is not an integer")
