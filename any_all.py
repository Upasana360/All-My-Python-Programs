# num1=[2,5,6,8,10]
# num2=list(range(1,7))
# # even=[]
# # for i in num1:
# #     even.append(i%2==0)
# # print(even)
# # this canbe done with thehelp of any and all fun:
# print(all([i%2==0 for i in num1]))
# print(any([i%2==0 for i in num1]))
#assignment
def my_sum(*args):
    #args=()
    if all([(type(arg)==int or type(arg)==float) for arg in args]):
        total=0
        for num in args:
            total+=num
        return total
    else:
        return "wrong input"
print(my_sum(1,2,3,4,3.8,"maggie"))
        
