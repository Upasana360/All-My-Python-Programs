#with reverse method
def reverse_list(l):
    num=[]
    for i in l:
        num.append(i)
        num.reverse()
    return num
list1=[1,6,7,8]
print(reverse_list(list1))