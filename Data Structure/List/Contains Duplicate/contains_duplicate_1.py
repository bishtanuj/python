# Program to find the duplicate elements in list

from collections import Counter

# function to check the duplicate elements in a list
def checkDuplicate(nums: list[int]) -> list[int]:
  # find the occurrence of the elements of list and saves them in a dictionary "occurrence" such that the elements are keys and their occurrences are the values respectively
  occurrence = Counter(nums)

  # append the elements in a list "K" whose values is greater than 1 in a dictionary "occurrence"
  K = [i for i in occurrence if occurrence[i] > 1]

  # return the list "K"
  return K


# driver function 
if __name__ == "__main__":
  numbers = list(map(int, input("Enter the numbers: ").split()))
  print(f"Numbers that occurs more than once in a list: {checkDuplicate(numbers)}")
  
