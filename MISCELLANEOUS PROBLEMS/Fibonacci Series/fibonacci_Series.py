# Program to print fibonacci series

# function to print the fibonacci series
def fibonacci_Series(num):
    if num == 1:
        return 0
    elif num == 2:
        return 1
    else:
        return fibonacci_Series(num-1) + fibonacci_Series(num-2)


# Driver Function 
if __name__ == '__main__':
    num = int(input("Enter the range of fibonacci series: "))
    print("Fibonacci Series: ")
    for i in range(1, num+1):
        print(fibonacci_Series(i), end=" ")

        

'''
OUTPUT:
Enter the range of fibonacci series: 20
Fibonacci Series: 
0 1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987 1597 2584 4181 
'''
