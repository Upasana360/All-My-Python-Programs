#enumerate is used with foor loop to track position
list1=['abc','abcd','abcdef','abbcggh','harshit']
#to find the position we can use for loop
# pos=0
# for name in names:
#     print(f"position is:{pos} and string is:{name}")
#     pos+=1
# print(names)
# #this can be done with enumerate func
# for pos,name in enumerate(names):
#     print(f"{pos}:{name}")

#assignment
#list containing string
#string that want to find in your list
#and this func will return the index of string in ur list and 
#if string is not present then return -1
def find_pos(l,target):
    for pos,name in enumerate(l):
        if name==target:
            return pos
        return -1
print(find_pos(list1,"harshit"))

