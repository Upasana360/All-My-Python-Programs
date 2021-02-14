winning_number=67
user_input=int(input('guess a number between 1 to 100:'))
if user_input==winning_number:
    print("you win!!!")
else :
    if user_input > winning_number:
        print("this numberis gretterthan winning number:")
    else:
        print("this number is less than wiing number")
