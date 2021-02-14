#list comprehension
#create a listof square from 1 to 10
square=[i**2 for i in range(1,11)]
print(square)
#list of -ve numbers
negative=[-i for i in range(1,11)]
print(negative)
#list having name 1st letter
names=['maggie','harry','ganesh','sujata']
new_list=[name[0] for name in names]
print(new_list)
