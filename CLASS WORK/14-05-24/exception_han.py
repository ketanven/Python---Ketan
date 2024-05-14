try:
    num = int(input("ENTER A NUMBER = "))
    print(num)

except ValueError as e:
    print("INVALID PLS ENTER A NUMBER ONLY    ",e)
    
    