# def func(item):
#     return len(item)
# name=['maggie','souravu','sujata','abc','xc']
# print(max(name,key=func))
# #this can also be done by lambda func
# name1=['maggie','souravu','sujata','abc','xc','harshit vasihistha']
# print(max(name1,key=lambda item:len(item)))
# student=[{'names':'upasana','score':90,'age':34},
# {'name':'upasana','score':60,'age':23},
# {'name':'harshit','score':45,'age':32}]
# print(min(student,key=lambda d:d['score']))
# print(min(student,key=lambda item:item.get('age'))['name'])
# print(max(student,key=lambda d:d['score']))
student1={
    'harshit':{'score':20,'age':54},
    'maggie':{'score':80,'age':48},
    'suji':{'score':50,'age':33}
}
print(max(student1,key=lambda item:student1[item]['score']))

