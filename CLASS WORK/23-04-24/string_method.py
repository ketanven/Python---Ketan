s= "TOPS TECHNOLOGIES"


print(len(s)) #TO FIND THE LENGTH OF THE STRING

print(type(s)) #TO FIND THE TYPE OF THE STRING

print(s.capitalize()) #TO CONVERT THE STRING INTO CAPITALIZE(ONLY FIRST LETTER INTO CAPITAL)

print(s.casefold()) #TO CONVERT THE STRING INTO SMALLER CASE

print(s.center(30,"*"))#TO PRINT THE STRING IN THE CENTER WITH SOME PATTERNS

print(s.find("T"),2)#TO FIND THE CHARCTERS OF THE STRING



print(s.isalnum())#CHECK THE STRING IS HAVING BOTH NUMBER AND STRING

print(s.isalpha())#CHECK THE STRING IS HAVING ALPAHABETES

print(s.index("T",3))#IT WILL PRINT THE EXACT INDEX OF THE STRING(STARTING = 0)

print(s.endswith("es"))

print(s.replace("T","W"))

print(s.lower())

print(s.count("T"))

print(s.swapcase())

print(s.startswith("T"))

print(s.format())


S1 = "-".join(s)
print(S1)