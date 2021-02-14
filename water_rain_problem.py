list1=[2,0,3]
res=0
for i in range(1,len(list1)-1):#outer loop
    i=1
    left=list1[i]#left=0
    for j in range(0,len(list1)-1):#inner loop1
        j=0
        left=max(left,list1[j])#left=3
        right=list1[i]#right=0 #1
        for j in range(i+1,len(list1)):#inner loop2
            j=2
            right=max(right,list1[j])#right=2
res=res+(min(left,right))-list1[i]
print(f"the amount we reserved is {res}")










