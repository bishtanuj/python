# Program to find the single occurred elements in a list

from collections import Counter

def singleOccurrence(num: list[int]) -> list[int]:
  occurrence = Counter(num)

  K = [i for i in occurrence if occurrence[i] == 1]
  return K
