#define a function that takes a number(n)
#return ictionary containing cube ofnumberfrom 1 to n
#example {1:1,2:8,3:27}
def cube_num(n):
    cube={}
    for i in range(1,n+1):
        cube[i]=i**3
    return cube
print(cube_num(3))
#word counter dictionary
def word_counter(s):
    count={}
    for i in s:
        count[i]=s.count(i)
    return count
print(word_counter("maggie"))