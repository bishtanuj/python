# Program to sort the list using bubble sort technique

# function to perform bubble sort
def bubble_sort(nums: list[int], size: int):
    for i in range(size - 1):
        for j in range(size - 1 - i):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]


# driver
if __name__ == '__main__':
    N = int(input("Enter the total number of elements: "))
    array = list(map(int, input(f"Enter the {N} element(s) of the list: ").split()))[:N]
    print(f"List: {array}")
    bubble_sort(array, N)
    print(f"Sorted List: {array}")


"""
OUTPUT:
Enter the total number of elements: 5
Enter the 5 element(s) of the list: 9 8 7 1 2
List: [9, 8, 7, 1, 2]
Sorted List: [1, 2, 7, 8, 9]
"""
