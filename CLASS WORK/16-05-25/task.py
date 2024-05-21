class Batsman:
    
    def fun1(self):
        self.name = input("--ENTER YOUR TEAM NAME = ")
        self.teamscore = int(input("ENTER YOUR TOTAL TEAM SCORE = "))
        self.batsmanname = input("--ENTER THE BATSMAN NAME = ")
        self.scoreofbatsman = int(input("TOTAL RUNS SCORED BY THIS BATSMAN = "))

class Data(Batsman):
    
    def fun2(self):
        self.nameofbowler = input("--ENTER THE BOWLER NAME = ")
        self.wickets = int(input("--ENTER TOTAL WICKETS TAKEN BY THIS BOWLER = "))
        self.manofthematch = input("--ENTER THE NAME OF MAN OF THE MATCH = ")

class Result(Data):
    def fun3(self):
        print()
        print("NAME OF THE TEAM IS", self.name)
        print("TOTAL RUNS SCORED BY THE TEAM IS = ", self.teamscore)
        print()
        
        print("BATSMAN NAME = ", self.batsmanname)
        print("TOTAL SCORE SCORED BY THE BATSMAN = ", self.scoreofbatsman)
        print()
        
        print("NAME OF THE BOWLER = ", self.nameofbowler)
        print("TOTAL WICKETS TAKEN = ", self.wickets)
        print()
        
        print("MAN OF THE MATCH = ", self.manofthematch)
        print()
            
        average = self.teamscore / 11
        print("AVERAGE OF THE ONE PLAYER IS = ", average)
        
obj = Result()
obj.fun1()
obj.fun2()
obj.fun3()
