list=[1,2,3,4,5]
def square_num(num):
    list1=[]
    for i in num:
        list1.append(i**2)
    return list1
print(square_num(list))