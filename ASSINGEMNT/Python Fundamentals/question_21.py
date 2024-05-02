def stringmultipleof4(s):
    if len(s) % 4 == 0:
        return s[::-1]  # Reverse the string using slicing
    else:
        return s  # Return the string unchanged if length is not a multiple of 4


input_string = "abcdefgh"
output_string = stringmultipleof4(input_string)
print(output_string)  # Output: "hgfedcba"

input_string2 = "hello"
output_string2 = stringmultipleof4(input_string2)
print(output_string2)  # Output: "hello"
