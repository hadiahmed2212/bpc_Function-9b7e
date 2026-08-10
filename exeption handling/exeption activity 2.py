try:
    num,num2=eval(input("enter 2 numbers seperated by commas DO NOT ADD A COMMA AT THE END OR START."))
    result= num / num2
    print("the result is:",result)
except ZeroDivisionError:
    print("YOU HAVE DIVIDED BY ZERO (which is not allowed)")
except SyntaxError:
    print("please seperate the numbers like this: 1,2 or 3,4")
except:
    print("wrong input please run again.")
else:
    print("nice number")
finally:
    print("heheheha")