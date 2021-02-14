def sub_list(l):
    count=0
    for i in l:
        if type(i)==list:
            count+=1
    return count
list1=[1,2,3,[89,3,2]]
print(sub_list(list1))