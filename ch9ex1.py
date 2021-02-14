#define a function that take list of string
#list containing reverse of everystring
def rever_string(l):
    return [i[::-1] for i in l]
print(rever_string(("abc","def","ghi")))
#list compresion with if statement
num= [1,2,3,4,5,6,7,8,9,10]
# even_list=[2,4,6,8,10]
# odd_list=[1,3,5,7,9]
even_num=[i for i in num if (i%2==0)]
print(even_num)
odd_num=[i for i in num if(i%2!=0)]
print(odd_num)
#num  to string
#from[true,false,1,2,1.0]
#print[1,1.0,2]
def num_fromstr(l):
    return[str(i) for i in l if(type(i)==int or type(i)==float)]
list1=["true","false",1,2,1.0]
print(num_fromstr(list1))
#LIST comprehension with if else statement
num1=list(range(1,11))
num1=[i**2 if i%2==0 else -i for i in num]
print(num1)
#l.c in nested list
#o/p=[[1,2,3],[1,2,3],[1,2,3]]
nested_list=[[i for i in range(1,4)]for j in range(3)]
print(nested_list)
#dictionary comprehension:
square={i:i**2 for i in range(1,11)}
print(square)
square1={f"square of {num} is ":{num**2} for num in range(1,11)}
print(square1)
for k,v in square1.items():
    print(f"key{k}:value{v}")
#to countthe occurance of char instring
string="upasana"
word_count={i:string.count(i) for i in string}
print(word_count)
#dictionary comprehension with if else 
odd_even={i:('even'if i%2==0 else'odd') for i in range(1,11)}
print(odd_even)
#set comprehension
s={i**2 for i in range(1,11)}
print(s)
names=['maggie','upasana','sujata']
first={name[0] for  name in names}
print(first)