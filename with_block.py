# use of with  block
# with open("file.txt")as f:
#     print(f.read())
with open("file.txt",'r+')as f:
    f.write("Upasana Majhi")
    print(f.read())
