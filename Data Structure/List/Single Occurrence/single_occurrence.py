# Program to find the single occurred elements in a list

from collections import Counter

def singleOccurrence(num: list[int]) -> list[int]:
  occurrence = Counter(num)

  K = [i for i in occurrence if occurrence[i] == 1]
  return K


if __name__ == "__main__":
  numbers = list(map(int, input("Enter the list of a numbers: ").split())
  print(f"Elements that occured once in a list: {singleOccurrence(numbers)}")
