user={'name':'upasana','age':24}
print(user)
user1=dict(name='upasana',age=23)
print(user1)
#how to access data from dictionary
print(user1['age'])
#Representation of dictionary
user_info={
    'name':"harshit",
    'age':23,
    'fav_movie':["coco",'toystory']
}
print(user_info)
print(user_info['fav_movie'])
#store dictionary inside dictionary
#how to add data to empty dictionary
num={}
num['name']='mohit'
num['age']=24
num['fav_movie']=['movie1','movie2']
print(num)
#in keyword and iteration in dictionary
if 'name' in num:
    print('present')
else:
    print("not present")
if 'mohit' in num.values():
    print("present")
else:
    print('not present')
#loop in dictionary
for i in num:
    print(i)
for i in num.values():
    print(i)
for i in num:
    print(num[i])
for i in num.items():
    print(i)
user_data=num.values()
print(user_data)
user_data=num.keys()
print(user_data)
user_data=num.items()
print(user_data)
print(type(user_data))
for i,j in num.items():
    print(f"key is:{i},value is:{j}")

