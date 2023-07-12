# Program to find the first missing positive element in a list


def firstMissingPositive(nums: list[int]) -> int:
  K = sorted(set(nums))
  i = 1
  for num in K:
    if num == i:
      i += 1
    elif num > 0:
      return i
  return i

