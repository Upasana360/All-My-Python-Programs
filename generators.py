#generators
#generators are iterators
# for num in map(lambda a:a**2,[1,2,3,4]):
#     print(num)
#     #generator is a sequence just like list
# def num(n):
#     for i in range(1,n+1):
#         yield(i)
# for number in num(10):
#     print(number)
# no=num(20)
# for number in no:
#     print(number)
# def num(n):
#     for i in range(1,n+1):
#         if (i%2==0):
#             yield(i)
# for number in num(10):
#     print(number)
# def num(n):
#     for i in range(1,n+1):
#         if i%2==0:
#          yield(i) 
# for i in num(10):
#     print(i)
#generator comprehension
# square=(i**2 for i in range(1,11))
# for i in square:
#     print(i)
# cube=(i**3 for i in range(1,11))
# for i in cube:
#     print(i)
# import time
# t1=time.time()
# l=[i**2 for i in range(100000000)]
# t2=time.time()
# total=t2-t1
# print(total)
# t1=time.time()
# l=(i**2 for i in range(100000000))
# t2=time.time()
# total=t2-t1
# print(total)
