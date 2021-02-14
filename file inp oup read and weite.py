with open("file.txt",'r')as rf:
    with open("file2.txt",'a')as wf:
        for line in rf.readlines():
            name,salary=line.split(',')
            wf.write(f"\n{name}\'s salary is{salary}")

