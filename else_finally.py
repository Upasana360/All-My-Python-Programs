while True:
    try:
        number=int(input("enter a number:"))
    except ValueError:
        print("may b u entered string instead of no try again")
    except:
        print("Unexcepted error...")
    else:
        print(f"user input={number}")
        break
    finally:
        print("____________Upasana Majhi_____________")