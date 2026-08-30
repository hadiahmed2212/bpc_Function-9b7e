def match (words):
    ctr=0
    list1= []
    for word in words:
        if len (word)>1 and word[0]==word [- 1]:
            ctr+=1
            list1.append(word)
    print("the list of words having the first and last character same",list1)
    return ctr
count=match(["aba","hadi","67","41"])
print ("count is",count)