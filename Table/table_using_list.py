# Program to print the table of a number using list

# function to print the table
def printTable(num: int):
  table = [i*num for i in range(1, 11)]
  k = 1
  for i in table:
    print(f"{num} * {k} = {i}")
    k += 1


# driver function
if __name__ == "__main__":
  num = int(input("Enter the number: "))
  printTable(num)


'''
OUTPUT:
Enter the number: 5
5 * 1 = 5
5 * 2 = 10
5 * 3 = 15
5 * 4 = 20
5 * 5 = 25
5 * 6 = 30
5 * 7 = 35
5 * 8 = 40
5 * 9 = 45
5 * 10 = 50
'''
