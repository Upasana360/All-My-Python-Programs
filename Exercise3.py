name,char=input("Enter ur name and which charyou want to count:").split(",")
print("lngth of username is"+str(len(name)))
print(f"lengthofuser nameis{len(name.strip())}")   
print(name.count(char))#case sensitive
#if we want to ignore this upper and lower case letter then we can do
print(f"the occourance of letter is{name.strip().lower().count(char.strip().lower())}")

