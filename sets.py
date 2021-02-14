s={1,2,3,4,5,6}
print(s)
print(type(s))
s.add(8)
print(s)
s.remove(1)
s2=print(set(range(1,11)))
s3=s.copy()
print(s3)
print(s3 is s)
print(s3==s)
s2=print(list(set(range(1,11))))
s.clear()
print(s)
s.discard(11)
print(s2)
#more about sets
#in keyword in sets and foor loop
s4={1,2,3,4,5,6}
s5={1,2,3,4,5,6,7,8,9}
for i in s4:
    print(i)
#set maths(union and intersection operation)
union_set=s4|s5
print(union_set)
intersection=s4 & s5
print(intersection)



