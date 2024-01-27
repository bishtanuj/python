# Program to calculate the absolute difference between the sums of diagonals of square matrix


def diagonal_difference(array: list[list[int]], size: int) -> int:
    diagonal_1, diagonal_2 = 0, 0
    for i in range(size):
        for j in range(size):
            if i == j:
                diagonal_1 += array[i][j]
            if i+j == size-1:
                diagonal_2 += array[i][j]

    difference = diagonal_2 - diagonal_1
    if difference < 0:
        return -difference
    else:
        return difference


if __name__ == '__main__':
    dimension = int(input("Enter the dimension of square matrix: "))
    matrix = []
    print("Enter the elements of square matrix:")
    for rows in range(dimension):
        matrix.append(list(map(int, input().rstrip().split())))
    print(f"Absolute difference of the diagonals of matrix: {diagonal_difference(matrix, dimension)}")
