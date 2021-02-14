name,age=input("enter ur name: and age:").split(",")
age=int(age)
if (name[0]=='a' or name[0]=='A') and age >=10:
    print("you can watch coco movie")
else:
    print("you can't watch coco movie")