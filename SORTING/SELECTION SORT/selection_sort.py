# Program to perform selection sort technique to sort the list

# function to perform selection sort
def selection_sort(nums: list[int], size: int):
    for i in range(size - 1):
        min_index = i
        for j in range(i + 1, size):
            if nums[j] < nums[min_index]:
                min_index = j
        if min_index != i:
            nums[i], nums[min_index] = nums[min_index], nums[i]


# driver
if __name__ == '__main__':
    N = int(input("Enter the total number of elements: "))
    num = list(map(int, input(f"Enter {N} element(s) of the list: ").split()))[:N]
    print(f"List: {num}")
    selection_sort(num, N)
    print(f"Sorted List: {num}")


"""
OUTPUT:
Enter the total number of elements: 5
Enter 5 element(s) of the list: 9 8 6 1 4
List: [9, 8, 6, 1, 4]
Sorted List: [1, 4, 6, 8, 9]
"""
