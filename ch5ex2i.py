def reverse_list(l):
    num=[]
    for i in l:
        num.append(i)
        rev=num[::-1]
    return rev
num1=[1,2,6,3,5,8]
print(reverse_list(num1))
