def add (number,number2):
    return number+number2
def sub (number,number2):
    return number-number2
def mult (number,number2):
    return number*number2
def div (number,number2):
    return number/number2
try:
    number = float(input("Enter first number"))
    number2 = float(input("enter second number"))
    choice = int(input("1 = addition 2= subtraction 3=multiplication 4= division"))
    if choice == 1:
        print(add(number,number2))
    elif choice == 2:
        print(sub(number,number2))
    elif choice == 3:
        print(mult(number,number2))
    else:
        print(div (number,number2))
except ValueError:
    print("please enter a NUMBER ONLY!")
except ZeroDivisionError:
    print("cannot divide by 0!")
