# Program to find whether the list contain duplicate elements or not
from collections import Counter

# function to check the duplicacy in the list
def contains_duplicate(nums: list[int]) -> bool:
  # find the frequency of each element in a list
  dict = Counter(nums)

  # if frequecy is greater than 1, return True else False
  for i in dict.values():
    if i > 1:
      return True
      break
  return False


# driver function
if __name__ == "__main__":
  # scan the list from the user
  numbers = list(map(int, input("Enter the number seperated by space: ").split()))
  
  # call the function and save its output in the valriable "result"
  result = contains_duplicate(numbers)
  if result:
    print("List contains duplicate elements")
  else:
    print("List doesnot contains duplicate elements")
