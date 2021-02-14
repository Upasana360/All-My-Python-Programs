name=input("enter ur name:")
repeat=" "
for i in range(0,len(name)):
    if name[i] not in repeat:
        repeat+=name[i]
        print(f"{name[i]:}{name.count(name[i])}")
    