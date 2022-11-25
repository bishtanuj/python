# Program to print the Tribonacci Series

# function to print the tribonacci series
def tribonacci_series(limit):
    if limit == 1 or limit == 2:
        return 0
    elif limit == 3:
        return 1
    else:
        return tribonacci_series(limit-1) + tribonacci_series(limit-2) + tribonacci_series(limit-3)


# Driver Function 
if __name__ == '__main__':
    
    # scanning the range of the tribonacci series 
    limit = int(input("Enter the range of tribonacci series: "))
    print("Tribonacci Series: ")
    for i in range(1, limit+1):
        print(tribonacci_series(i), end=" ")

        
        
'''
OUTPUT:
Enter the range of tribonacci series: 20
Tribonacci Series: 
0 0 1 1 2 4 7 13 24 44 81 149 274 504 927 1705 3136 5768 10609 19513 
'''
