ttl_HW= 7
orgin_cnt= ttl_HW
print(f"you have about {orgin_cnt} homework remaining please complete it.")
com_cnt=0
taskn=1
while taskn <= ttl_HW:
    if taskn == 1:
        print("do your math homework")
    elif taskn == 2:
        print("do your english homework")
    elif taskn == 3:
        print("up next grammar and reading homework")
    else:
        nxttsk="coding class"
    ans= (input(f"have you finished {nxttsk}? yes or no?"))
    if ans== "yes":
        com_cnt+= 1
        taskn+=1
        print("NICE! ,keep it up.")
    else:
        print("NOPE, finish it or else.")

    print("tasks that remain.", ttl_HW-com_cnt)
    print()

    print(" ALL HOMEWORK COMPLETED!")
    print("NICE!")
    