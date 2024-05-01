from package1 import*
while True:
    
    menu = """
    select your choice
    1) for reverse the string
    2) for length of the string
    3) for middle of the string
    4)exit

    """
    print(menu)

    choice = int(input("SELECT YOUR CHOICE"))
    if choice == 1:
     reverse()
    
    elif choice == 2:
     slen()
    elif choice == 3:
     middle()
    elif choice == 4:
     print("THANKS FOR USING ")
     break
    else:
     print("invalid choice")
     break