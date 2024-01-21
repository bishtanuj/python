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

  # create a list 'result' that contains the elements that occurred only once in num
  result = [key for key in occurrence if occurrence[key] == 1]
  return result

# driver function
if __name__ == '__main__':
  # scan the list from the user
  array = list(map(int, input("Enter the elements of the list: ").split()))

  # Print the conclusion
  print(f"List of elements that occurred only once in the array: {single_occurrence(array)}")
