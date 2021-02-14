# numbers=[1,2,3,4]
# def square(a):
#     return a**2
#  square=list(map(square,numbers))
# print(square)
# #this can be also done with lambda fun
# numbers1=list(range(1,11))
# square1=list(map(lambda i:i**2,numbers1))
# print(square1)
# #whith listcomprehension
# square2=[i**2 for i in numbers]
# print(square2)
# #this can also be donewith loop
# new_list=[]
# for num in numbers:
#     new_list.append(square(num))
# print(new_list)

name_list=['maggie','upasana','sujata patra','ganesh']
length=(map(len,name_list))
for i in length:
    print(i)
#technically map object is an iterator
for j in length:
    print(j)