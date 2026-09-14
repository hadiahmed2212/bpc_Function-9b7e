snack_box1={"chips","nuts","chocolate","cookies","milo"}
snack_box2={"chips","kinder","peanuts","weet-bix","dairy milk"}
print(f"snack box 1 {snack_box1} yummy!")
print(f"snack box 2 {snack_box2} yummy!")
snack_box1.add("kit-kat")
print("snack box 1 after adding a kit-kat",snack_box2)
common_candy=snack_box1.intersection(snack_box2)
print("common snacks in both boxes:",common_candy)
import array as arr
snackcnt=arr.array('i', [1,4,6,3])
print("snack count array:",snackcnt)
snackcnt.insert(2,5)
snackcnt.append(9)
print("snack count after adding some more snacks:",snackcnt)
cnt2= snackcnt.count (2)
print("number of 2s in snack box:",cnt2)
snackcnt.reverse()
print("reverse count of array",snackcnt)
