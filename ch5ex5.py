def common_element(l,k):
    list1=[]
    for i in l:
        for j in k:
            if i==j:
                list1.append(i)
    return list1
num=[1,2,5,8]
num1=[1,2,7,6,8]
print(common_element(num,num1))

