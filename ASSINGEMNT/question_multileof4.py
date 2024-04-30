def reverse_string_if_multiple_of_4(s):
    if len(s) % 4 == 0:
        return s[::-1]  # Reverse the string using slicing
    else:
        return s  # Return the string unchanged if length is not a multiple of 4

# Example usage:
input_string = "abcdefgh"
output_string = reverse_string_if_multiple_of_4(input_string)
print(output_string)  # Output: "hgfedcba"

input_string2 = "hello"
output_string2 = reverse_string_if_multiple_of_4(input_string2)
print(output_string2)  # Output: "hello"
