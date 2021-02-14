with open("output.txt",'r',encoding="utf-8")as rf:
    data=rf.readline()
    while len(data)>0:
        print(data)
        print(rf.encoding)
        data=rf.read(2)