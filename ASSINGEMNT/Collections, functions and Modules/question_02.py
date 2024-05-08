# Write a Python program to count the number of strings where the string
# length is 2 or more and the first and last character are same from a given
# list of strings.



def check(strings):
    count = 0
    for s in strings:
        if len(s) >=2 and s[0] == s[-1]:
            count += 1
    return count


list = ["abc","aba","ketan","pillai","uday","rajput","222302","11223344","task"]

print("Number of strings where the first and last character are the same:", check(list))
