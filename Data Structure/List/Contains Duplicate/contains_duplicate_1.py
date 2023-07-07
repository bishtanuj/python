# Program to find the duplicate elements in list

from collections import Counter


def checkDuplicate(nums: list[int]) -> list[int]:
  occurrence = Counter(nums)
  K = [i for i in occurrence if occurrence[i] > 1]
  return K



if __name__ == "__main__":
  numbers = list(map(int, input("Enter the numbers: ").split()))
  print(f"Numbers that occurs more than once in a list: {checkDuplicate(numbers)}")
  
