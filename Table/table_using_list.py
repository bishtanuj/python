# Program to print the table of a number using list

# function to print the table
def printTable(num: int):
  table = [i*num for i in range(1, 11)]
  k = 1
  for i in table:
    print(f"{num} * {k} = {i}")
    k += 1


if __name__ == "__main__":
  num = int(input("Enter the number: "))
  printTable(num)
