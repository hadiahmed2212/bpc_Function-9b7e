print("hi, welcome to the snack vending machine here you can get biscuits, chips and even drinks!! so go on if your hungry buy something!")
def cal_change (price,total_paid):
    change= price-total_paid
    return change
biscuits_pr=3.75
chips_pr=3.75
drinks_pr=4
print("THE ACCEPTED COINS ARE 5C,20C,50C,100C,200C")
ttl_insert=0
coin_insert=0
while True:
    coin=int(input("Please put a coin in the compartment below to start."))
    if coin !=5 and 20 and 50 and 100 and 200:
        print("INVALID COIN (IT IS COMING OUT FOR THE COMPARTMENT BELOW THE COMPARTMENT BELOW THE COIN INSERTING THINGY)")
        continue
    coin_insert += (coin_insert)
    ttl_insert += (ttl_insert)

