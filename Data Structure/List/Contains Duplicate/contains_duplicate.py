from collections import Counter

def contains_duplicate(nums: list[int]) -> bool:
  dict = Counter(nums)
  for i in dict.values():
    if i > 1:
      return True
      break
  return False


if __name__ == "__main__":
  numbers = list(map(int, input("Enter the number seperated by space: ").split()))
  result = contains_duplicate(numbers)
  if result:
    print("List contains duplicate elements")
  else:
    print("List doesnot contains duplicate elements")
