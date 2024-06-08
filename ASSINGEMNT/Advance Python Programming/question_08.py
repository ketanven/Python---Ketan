# Write a Python program to count the number of 
# lines in a text file.

def count():
    line_counter = 0
    file = open("python.txt", 'r')
    for i in file:
            line_counter += 1
    return line_counter


lines = count()

# Print the number of lines to verify
print("Number of lines:", lines)
    
