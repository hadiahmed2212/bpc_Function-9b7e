valid = False
while not valid:
    try:
        num=int(input("enter a number -_-"))
        while num %2==0:
            print("goodbye forever...")
        valid= True
    except ValueError:
        print("INVALID NUMBER")
            