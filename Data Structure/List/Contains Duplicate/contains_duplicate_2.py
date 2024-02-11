# Program to find duplicate element in the list

# function to find the duplicate in the list
def find_duplicates(nums: list[int]) -> list[int]:
    frequency = {}
    for element in nums:
        key = frequency.keys()
        if element in key:
            frequency[element] += 1 
        else:
            frequency[element] = 1
    
    duplicate = [key for key in frequency if frequency[key] > 1]
    return duplicate


# driver
if __name__ == '__main__':
    # scan the list of numbers from the user
    numbers = list(map(int, input("Enter the elements of the list: ").split()))

    # print the list of duplicate elements
    print(f"Duplicate elements in the list: {find_duplicates(numbers)}")
    
