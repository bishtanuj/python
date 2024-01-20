# Program to compute the subarray of the array

def compute_subarray(array: list[int]) -> list[list[int]]:
    length = len(array)
    subarray = []
    for start in range(length):
        for end in range(start+1, length+1):
            subarray.append(array[start:end])
    return subarray


if __name__ == '__main__':
    arr = list(map(int, input("Enter the elements of the array: ").split(" ")))
    print(f"List of all subarray: {compute_subarray(arr)}")
