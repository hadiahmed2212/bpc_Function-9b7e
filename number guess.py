import random
number= str (random.randint(1,3))
print("i have picked a random number between 1 and 3 try to guess the number.")
playing=True
while playing:
    guess=(input("now you can guess the number."))
    if number == guess:
        print("Nice you guessed the number")
        break
    else:
        print("sad,please try again.")
        