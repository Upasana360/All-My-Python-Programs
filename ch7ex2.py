user={}
name=input("enterur name")
age=input("enter ur age")
fav_movie=input("enterthe movies u likeseparated by comma:").split(",")
fav_song=input("enter the songs that u like separated by comma").split(",")
user['name']=name
user['age']=age
user['fav_movie']=fav_movie
user['fav_song']=fav_song
print(user)
for k,v in user.items():
    print(f"key:{k} vale:{v}")