# def square(a):
#     '''this func return square of number'''
#     return a**2
# square1=square#here fun is assigned not called
# print(square1(2))
# print(square(2))
# print(square)
# print(square1)
# print(square.__doc__)
# print(square1.__doc__)
# print(square.__name__)
# print(square1.__name__)
#pass function as argument
#--------------------------------
# def square(a):
#     return a**2
l=[1,2,3,4,5]
# print(list(map(square,l)))
#This can be done with the help of lambda function
print(list(map(lambda a:a**3,l)))





