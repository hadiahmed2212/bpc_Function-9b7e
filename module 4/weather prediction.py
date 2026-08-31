weather= (1,1,1,0,0,0,0)
sunny=0
rainy=0
for i in range (0,7):
    if weather[i]==0:
        rainy +=1
    else:
        sunny +=1

if rainy >sunny:
    print("bad weather(it will rain)")
else:
    print("good weather(sunny weather)")

