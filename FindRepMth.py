string="She is the color is blue"
print(string.replace(" ","_"))
print(string.replace("is","are",1))
print(string.find("is"))
print(string.find("is",5))
is_pos1=string.find("is")
is_pos2=string.find("is",is_pos1+1)
print(is_pos2)