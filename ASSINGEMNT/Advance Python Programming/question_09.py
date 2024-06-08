#Write a Python program to count the frequency of words in a file.

word = "some"
count = 0
file = open("python.txt", 'r')
for line in file: 
		words = line.split() 
		for i in words: 
			if(i==word): 
				count=count+1
print("Occurrences of the word", word, ":", count)
