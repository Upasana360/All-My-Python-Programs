def is_greater(a,b):
    if a>b:
        return a 
    return b 
def greatest(a,b,c):
    bigger=is_greater(a,b)
    print(is_greater(bigger,c))
greatest(7,3,6)