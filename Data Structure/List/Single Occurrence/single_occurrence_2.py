# Program to find the single occured elements in a list

# function to find the element that only occured once
def single_occurrence(num: list[int]) -> list[int]:
  # create the dictionary 'occurrence' having elements of a num as keys and their occurrences as their values respectively
  occurrence = {}
  for element in num:
    key = occurrence.keys()
    if element in key:
      occurrence[element] += 1
    else:
      occurrence[element] = 1
      
  result = [key for key in occurrence if occurrence[key] == 1]
  return result


if __name__ == '__main__':
  array = list(map(int, input().split()))
  print(f"{single_occurrence(array)}")
