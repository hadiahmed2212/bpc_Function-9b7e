habit_info=("reading", False,4,6.7)
print(habit_info)
weekly_habits= (0,1,0,1,0,1,0)
print(weekly_habits)
print("Days tracked:",len(weekly_habits))
print("day 1:",weekly_habits[0])
print("day 4:",weekly_habits[3])
first3_days= weekly_habits[0:3]
print(f"The first three days have been good {first3_days} Keep it up!")
weekend_days= weekly_habits [5:7]
print(f"The weekend days are also good {weekly_habits} NICE!")
weekly_habits = weekly_habits +(1,)
print("After adding another day:",weekly_habits)
completed =weekly_habits.count(1)
missed = weekly_habits.count(0)
print("completed days:",completed)
print(f"missed days: {missed}Oh No!")
done=0
not_done=0
for i in range (0,len (weekly_habits)):
    if weekly_habits [i]==1:
        done += 1
    else:
        not_done += 1
if done > not_done:
    print("Nice,keep it up")
else:
    print(" Oh No! Get better")



