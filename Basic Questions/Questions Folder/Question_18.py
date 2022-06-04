# Write a program to count the number of characters in a string

string_1 = input("Enter a string: ")
count = 0

for i in range(0, len(string_1)):
    if string_1[i] != " ":
        count += 1

print("Total characters in given string:", count)


# OUTPUT
# Enter a string: Anuj Bisht
# Total characters in given string: 9
