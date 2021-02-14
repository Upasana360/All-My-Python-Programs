from functools import wraps
def decorator_fun(anyfunc):
    '''this is decorator fun'''
    @wraps(anyfunc)
    def wrapper_fun(*args,**kwargs):
        '''this is wrapper function'''
        print("This is awesome function")
        return anyfunc(*args,**kwargs)
    return wrapper_fun
def func1(a):
    '''this is func1'''
    print("this is in func1")
    return a**2
var=decorator_fun(func1)
print(var(3))
def func2():
   print("this is in func2")
var=decorator_fun(func2)
var()
#this can also be implemented in another way
@decorator_fun
def func3(a,b):
   print("this is in func3")
   return a+b
print(func3(2,3))
print(func1.__doc__)
print(func1.__name__)
print(decorator_fun.__doc__)


#this func can be solved by import wraps




