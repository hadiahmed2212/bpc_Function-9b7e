def factorial_num (x):
    '''this is the function that calculates the factorial of the number.'''
    if x==0 or x==1:
        return 1
    else:
        return x*factorial_num(x-1)
print(factorial_num.__doc__)
x=int(input("enter a number you want to calculate the factorial for."))
print("the factorial of the number you entered is...",factorial_num(x))