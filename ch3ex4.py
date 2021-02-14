sum=0
i=0
num=input("enter number containg more than one digit:")
num1=(len(num))
while i<=num1-1:
    sum=sum+int(num[i])
    i+=1
print(sum)


