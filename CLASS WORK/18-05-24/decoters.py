def hello(fv):
    def fvx():
        print("WELCOME TO OUR WEBSITE*")
        fv()
        print("THANK YOU FOR USING OUR WEBSITE**")
        
    fvx()
@hello
def fac():
    fac = 1
    num = int(input("ENTER A NUMBER FOR FAC = "))
    for i in range(1,num+1):
        fac*=i
    
    print(fac)
