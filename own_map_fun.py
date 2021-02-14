# def my_map(fun,l):
#     new_list=[]
#     for item in l:
#         new_list.append(fun(item))
#     return new_list
# print(my_map(lambda a:a**2,[1,2,3,4,5]))
#function returning function
# def outer_fun(msg):
#     def inner_fun():
#         print(f"The message is :{msg}")
#     return inner_fun
# variable=outer_fun("hiii bob")
# variable()
#this is also called closures
def outer_fun(x):
    def inner_fun(n):
      return x**n
    return inner_fun
variable=outer_fun(3)
print(variable(3))



        

