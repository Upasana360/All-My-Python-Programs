def func(int1,int2):
    add=int1+int2
    mul=int1*int2
    return add,mul
add,mul=func(2,3)
print(add)
print(mul)
#something more about touple list and string
nums=tuple(range(1,11))
print(nums)
print(type(nums))
num1=str((1,2,3))
print(num1)
print(type(num1))
num_list=str([1,2,3,4])
print(type(num_list))