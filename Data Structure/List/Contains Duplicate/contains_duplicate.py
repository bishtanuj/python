import collections import Counter

def contains_duplicate(nums: list[int]) -> bool:
  dict = Counter(nums)
  for i in dict.values():
    if i > 1:
      return True
      break
  return False

