# Program to print the Tetranacci Series

# function to print the tetranacci series
def tetranacci_series(limit):
    if limit == 1 or limit == 2 or limit == 3:
        return 0
    elif limit == 4:
        return 1
    else:
        return tetranacci_series(limit-1) + tetranacci_series(limit-2) + tetranacci_series(limit-3) + tetranacci_series(limit-4)


# Driver Function 
if __name__ == '__main__':
    
    # scanning the range of the tetranacci series 
    limit = int(input("Enter the range of tetranacci series: "))
    print("Tetranacci Series: ")
    for i in range(1, limit+1):
        print(tetranacci_series(i), end=" ")

        

'''
OUTPUT:
Enter the range of tetranacci series: 20
Tetranacci Series: 
0 0 0 1 1 2 4 8 15 29 56 108 208 401 773 1490 2872 5536 10671 20569 
'''
