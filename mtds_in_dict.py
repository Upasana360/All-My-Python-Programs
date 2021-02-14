user=dict.fromkeys(['name','age'],'unnknown')
print(user)
user1=dict.fromkeys(['name','age'],['unknown','unknown'])
print(user1)
user2=dict.fromkeys(['name'],24)
print(user2)
d=dict.fromkeys(range(1,11),'upa')
print(d)
#getmethod(USEFUL)
print(user1['name'])
# print(user1('names'))
print(user1.get('name'))
print(user1.get('names'))
#loop type
if 'name' in user1:
    print('present')
else:
    print('absent')
#in get method
if user1.get('name'):
    print('present')
else:
    print('absent')
#clear method
d.clear()
print(d)
#copy mtd
user5=user1.copy()
print(user5)
print(user1)
print(user5 is user1)
#more about get()
# #if we want to get non -ve value
user6={'name':'upasana','age':23,'movies_like':['movie1','movie2']}
print(user6.get('name','not present!'))
print(user6.get('names','not present!'))

