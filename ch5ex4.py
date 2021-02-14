def odd_even(l):
    list1=[]
    list2=[]
    for i in l:
        if (i%2==0):
            list1.append(i)
        else:
            list2.append(i)
        list3=[list2,list1]
    return list3
list5=[1,2,3,4,5,6,7,8,9]
print(odd_even(list5))