add=lambda a,b:a+b
print(add(2,3,))
is_even=lambda i:i%2==0
print(is_even(7))
print(is_even(8))
def func(s):
    if len(s)>5:
        return True
    return False
print(func('maggie'))
#this can be also written in lambda
func=lambda s:len(s)>5
print(func('maggie'))
#lambda with if else
func1=lambda s:True if len(s)>5 else False
print(func1('maggie'))
