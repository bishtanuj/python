# Program to check whether given number is even or odd

# Function to check odd - even
def checkOddEven(a):
    if(a % 2 == 0):
        print(a,"is an even number.")
    else:
        print(a,"is an odd number.")

# Scanning the number
a = int(input("Enter a number: "))

# Calling checkOddEven function
checkOddEven(a)
