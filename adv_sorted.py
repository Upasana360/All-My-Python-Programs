# fruits=['grapes','apple','kiwi']
# fruits.sort()
# print(fruits)
# fruits=('banana','apple','kiwi')
# print(sorted(fruits))
# print(fruits)
# guitars=[{'model':'yamahaf310','price':8400},{'model':'faith naptune','price':6700},{'model':'taylor 814ce',"price":7800}]
# print(sorted(guitars,key=lambda d:d['price'],reverse=True))
# student1={
#     'harshit':{'score':20,'age':54},
#     'maggie':{'score':80,'age':48},
#     'suji':{'score':50,'age':33}
# }
# print(sorted(student1,key=lambda item:student1[item]['score']))
#more about function
def add(a,b):
    """this will add two numbers"""
    return a+b
print(add(2,3))
print(add.__doc__)
print(add.__name__)

