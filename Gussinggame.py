import random
winning_no=random.randint(1,100)
guess=1
while True:
    num=int(input("enter a number"))
    if num==winning_no:
        print(f"u win, ang ur guessed this no in time{guess}time")
        break
    else:
        if  num>winning_no:
            print("too high")
        else:
            print("too low")
        guess+=1
        continue
        
        
    
