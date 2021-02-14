f=open(r"E:\hi.txt")
lines=f.readlines()
for line in lines[0:2]:
    print(line,end='')

f.close()