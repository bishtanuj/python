# Write a program to reverse a string

'''
Test case
Input: My.name.is.Anuj
Output: Anuj.is.name.My
'''

# Scan a string
string = input("Enter a string: ")

# Split the string form "."
split_string_list = string.split(".")

# Reverse the split_string_list
reverse_list = split_string_list[::-1]

# Printing the result
count = 0
print("Result: ", end="")
for i in range(len(reverse_list) - 1):
    print(reverse_list[i]+".",end="")
    count = i+1
print(reverse_list[count])


# Time complexity: O(n)
