# Program to find first and last position of target in array


# function to find the first and last position of target
def first_last_position(nums: list[int], target: int) -> list[int]:

    # append the indexes form array to ans where element == target
    ans = [i for i in range(len(nums)) if nums[i] == target]

    # if ans == True (has values)
    if ans:
        return [ans[0], ans[len(ans) - 1]]
    # if ans == False (empty)
    else:
        return [-1, -1]


if __name__ == "__main__":

    # scan the number of elements of array
    nums_elements = int(input("Enter the number of elements of array: "))

    # scan the elements of array
    elements = list(map(int, input(f"Enter the {nums_elements} elements: ").split()))[:nums_elements]
    
    # print the array
    print(f"Array: {elements}")
    
    # scan the target element
    target_element = int(input("Enter the target element: "))
    
    # print the result
    print(f"Result: {first_last_position(elements, target_element)}")


    
    
```
OUTPUT:

```
