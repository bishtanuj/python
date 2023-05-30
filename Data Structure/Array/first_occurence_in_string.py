# Program to find the index of the first occurrence in a string

# Function to find the index of the first occurrence in a string
def stringInString(str1: str, str2: str) -> int:
    if str2 in str1:
        return str1.index(str2)
    return -1


# driver function
if __name__ == "__main__":
    # scan string1
    string1 = input("Enter first string: ")

    # scan string2
    string2 = input("Enter second string: ")

    # call the stringInString function and saves the value in result variable
    result = stringInString(string1, string2)

    # print the conclusion
    if result != -1:
        print(f"Index of first occurrence: {result}")
    else:
        print(f"{string2} is not a part of {string1}")
        
        
  
```
OUTPUT:
Enter first string: happyandhappy
Enter second string: happy
Index of first occurrence: 0
```


