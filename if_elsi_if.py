age=int(input("enter ur age:"))
if age<=0:
    print("u r noteligible to watch movie")
elif 1<=age<=3:
    print("ticket price:Free")
elif 4<=age<=10:
    print("ticket price:150")
elif 11<=age<=60:
    print("ticket price:250")
else:
    print("ticket price:200")