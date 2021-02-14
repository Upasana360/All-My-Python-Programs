list=[]
for i in range(1,11):
    list.append(i)
    print(list)
def neg_list(num):
    negative=[]
    for i in num:
        negative.append(-i)
    return negative
print(neg_list(list))