# Write a program to print the series of prime numbers in the given range by user using user defined function

# Function to print the range of prime numbers
def prime_number(lower, upper):
    for number in range(lower, upper + 1):
        if number > 1:
            for i in range(2, number):
                if number % i == 0:
                    break
            else:
                print(number, end=" ")


if __name__ == "__main__":
    # scanning the limits of the range from the user
    lower_limit = int(input("Enter the lower limit: "))
    upper_limit = int(input("Enter the upper limit: "))

    if lower_limit <= 0 or upper_limit <= 0:
        print("Enter positive number as a limit")
    else:
        # printing the required range of the prime numbers
        print(f"Prime numbers within range of {lower_limit} &{upper_limit}:")
        prime_number(lower_limit, upper_limit)

        
# OUTPUT
# Enter the lower limit: 10
# Enter the upper limit: 20
# Prime numbers within range of 10 &20:
# 11 13 17 19 

