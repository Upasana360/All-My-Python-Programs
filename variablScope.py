x=5
def fun():
    global x
    x=9
    return x
print(x)
print(fun())
print(x)
