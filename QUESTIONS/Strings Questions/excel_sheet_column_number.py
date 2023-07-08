# Program to print the excel sheet column number

def titleNumber(column: str) -> int:
  result = 0
  numbers = [i for i in range(1, 27)]
  letters = "ABCDEFGHIJHKLMNOPQRSTUVWXYZ"
  dictionary = dict(zip(letters, numbers))
  for i in column:
    result = result * 26 + dictionary[i]
  return result
  

if __name__ == "__main__":
  column = input("Enter the column of excel:" )
  print(f"Column Number: {titleNumber}")
