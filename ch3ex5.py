name=input("Enter ur name:")
i=0
repeat=" "
while i<len(name):
    if name[i] not in repeat:
        repeat+=name[i]
        print(f"{name[i]}:{name.count(name[i])}")
    i+=1