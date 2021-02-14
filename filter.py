numbers=list(range(1,11))
even=list(filter(lambda a:a%2==0,numbers))
print(even)
odd=list(filter(lambda i:i%2!=0,numbers))
print(odd)
# ITERATORS AND ITERABLE
numbers=[1,2,3,4]#tuple,string are iterators
square=tuple(map(lambda i:i**2,numbers))
print(square)
num=iter(numbers)
print(next(num))
print(next(num))
print(next(num))
print(next(num))

