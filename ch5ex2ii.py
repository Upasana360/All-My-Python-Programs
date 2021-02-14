def reverse_list(l):
    num=[]
    for i in range(0,len(l)):#(1,len(l)+1)
      popped_item=l.pop()
      num.append(popped_item)
    return num
list1=[1,2,3,4,5,6]
print(reverse_list(list1))