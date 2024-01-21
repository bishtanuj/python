# Program to find the single occurred elements in a list

from collections import Counter

# function to find the elements that occurred only once
def singleOccurrence(num: list[int]) -> list[int]:
  # create a dictionary "occurrence" having the elements of a num as Keys and their occurrence as their values respectively
  occurrence = Counter(num)

  # create a list K that contains the elements that occured only once in num
  K = [i for i in occurrence if occurrence[i] == 1]
  return K


# driver function
if __name__ == "__main__":
  # scan the list from the user
  numbers = list(map(int, input("Enter the list of a numbers: ").split())

  # print the conclusion
  print(f"Elements that occured once in a list: {singleOccurrence(numbers)}")


                 
'''
OUTPUT:
Enter the list of a numbers: 1 2 3 1 2 3 0 1 2 4 5 6 8 9 0 1 3
Elements that occured once in a list: [4, 5, 6, 8, 9]
'''
                 
