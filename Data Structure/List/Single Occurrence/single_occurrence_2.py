# Program to find the single occured elements in a list

# function to find the element that only occured once
def single_occurrence(num: list[int]) -> list[int]:
  # create the dictionary 'occurrence' having elements of a num as keys and their occurrences as their values respectively
  occurrence = {}
  for i in num:
    key = occurrence.keys()
    if i in key:
      occurrence[i] += 1
    else:
      occurrence[i] = 1
  return occurrence


