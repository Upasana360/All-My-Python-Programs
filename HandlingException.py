#Exception Handling
#try Exception else finally
#Exception are thoseerrors which comein the time of exection
while True:
    try:
        age=int(input("enter ur age:"))
        break
    except ValueError:
        print("may b u entered string instead of no try again")
    except:
        print("Unexcepted error...")
if age<18:
    print("you can't play the game")
else:
    print("you can play the game")
