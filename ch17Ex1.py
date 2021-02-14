def divide(a,b):
    try:
        return a/b
    except ZeroDivisionError as err:
        print(err)
    except TypeError as arr:
        print("number must be integer or float")
    except:
        print("unexpected err")

print(int(divide(12,2)))