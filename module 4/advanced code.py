items= ["pencil","eraser","whiteout","pen","fineliner"]
stck_cnts= [4,7,2,0,5]
inventory={item: count for item,count in zip(items, stck_cnts)}
print("full inventory is:", inventory)
in_stck_itms=[item for item in items if inventory[item] >0]
print(f"the in stock items are: {in_stck_itms} ")
chosen_item=(input("what would you like to buy?"))
if chosen_item not in inventory:
    print(" PLEASE ENTER SOMETHING WE HAVE!")
    exit()
price= [2,2,4,3,3.50]
price2= float(input("enter how much you would like the prices for all the items in stock to be?"))
marked_prcs= list(map(lambda p: p+ price2,price))
print("the updated prices are:", marked_prcs)
inventory[chosen_item]= inventory[chosen_item]-1
print(chosen_item,"PURCHASED! remaining stock:", inventory[chosen_item])

print("")
print("--------- SCHOOL STATIONARY STOCK CHECKER---------")
print("item bought today:", chosen_item)
print("price paid:", price2)
print("updated stock/inventory:",inventory)
print("--------------------------------------------------")
