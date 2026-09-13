basket1={"banana","apple","apple","mango"}
basket2={"mango","kiwi"}
print(basket1)
print(basket2)
basket2.add("strawberry")
basket2.add("peach")
print(basket2)
common_fruits=basket1.intersection(basket2)
print(common_fruits)
import array as arr
a=arr.array ('i',[1,2,4,5,4,6,3,4,5])
print(a)
a.insert(0,4)
a.append(9)
print(a)
cnt=a.count(4)
a.reverse()
