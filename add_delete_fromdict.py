userdata={'name':'upasana',
'age':23,
'fav_movie':['movie1','movie2']}
print(userdata)
#how to add data to dictionary
userdata['songs']=['song1','song2','song3']
print(userdata)
userdata['age1']=24
print(userdata)
#pop method
popped_item=userdata.pop('fav_movie')
print(userdata)
print(popped_item)
popped=userdata.popitem()
print(userdata)
print(popped)
#updata dictionary
more_info={'cook':['cake','biryani','gupchup']}
userdata.update(more_info)
print(userdata)
userdata.update({})
print(userdata)
