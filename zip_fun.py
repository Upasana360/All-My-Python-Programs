#it is a built in function
userid=['user1','user2','user3']
name=['maffie','upa','harshit']
print(tuple(zip(userid,name)))
#*operator withzip()
#here we would reverse the previous oprator
l=[(1,6),(2,3),(4,5)]
l1,l2=(list(zip(*l)))
print(l1)
print(l2)
#assignment zip two diff lstl1 and l2 then find the maxbetween the two lists element 
list1=[1,2,3,4]
list2=[3,1,4,2]
new=[]
for pair in zip(list1,list2):
    new.append(max(pair))
print(new)


