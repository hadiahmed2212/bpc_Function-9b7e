student_data={"hadi": 92, "hafi":96, "sam":0, "dude": 76, "joey": 83}
names = list(student_data.keys())
score=0
i = 0
total = 0
highest=0
lowest=0
while i < len(names):
    name = names[i]
    total = total + student_data[name]
    i = i + 1
    score = student_data[name]
    if score > highest:
        highest = score
    if score < lowest:
        lowest = score
print("The highest score is:", highest)
print("The lowest score is:", lowest)
average = total / len(student_data)
print("The average is:", average)