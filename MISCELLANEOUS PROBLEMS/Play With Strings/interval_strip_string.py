# Program to print the string after stripping the string at continuous intervals

# Scan the length of string
length_of_string = int(input("Enter the length of string: "))

# Scan the string 
string = input(f"Enter the string of length {length_of_string}: ")[:length_of_string]

# Print the result
print(string[0], end="")
i = 1
while i < length_of_string:
    if i % 4 != 0:
        print(string[i], end="")
    else:
        print()
        print(string[i], end="")
    i += 1


```
OUTPUT:
Enter the length of string: 26
Enter the string of length 26: ABCDEFGHIJKLMNOPQRSTUVWXYZ
ABCD
EFGH
IJKL
MNOP
QRST
UVWX
YZ
```
