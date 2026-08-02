name=(input("what is your name?"))
def greeting():
    print("Hi, welcome to the lemonade stand")
    print("MAKE YOUR ORDER!!")
greeting()
price_per_cup=float(input("what is the price per cup?"))
cups_sold=int(input("how many cups were sold?"))
def cal_ttl(price,cup):
    total= (price * cup)
    return total
ttl_cost= cal_ttl(price_per_cup,cups_sold)
rnd_ttl=round(ttl_cost,2)
print("your total cost is ",rnd_ttl)
paid= float(input(f"enter the amount paid by  {name}"))
def cal_change(paid,total):
    change = total-paid
    return change
change_due= cal_change(ttl_cost,paid)
print("your change is: ", round (change_due,2))
print("Nice doing buisness with you.")
