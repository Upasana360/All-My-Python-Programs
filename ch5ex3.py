def reverse_list(l):
    num=[]
    for i in l:
        num.append(i[::-1])
    return num
num1=['abc','def']
print(reverse_list(num1))
