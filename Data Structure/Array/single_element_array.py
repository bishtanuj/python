# HackerRank Problem
# Program to find the elements that occurs only once in an array

def lonely_integer(integer_list: list[int]) -> list[int]:
    frequency = {}
    for i in integer_list:
        key = frequency.keys()
        if i in key:
            frequency[i] += 1
        else:
            frequency[i] = 1

    lonely_numbers = [j for j in frequency if frequency[j] == 1]
    return lonely_numbers


if __name__ == '__main__':
    integers = list(map(int, input("Enter the numbers: ").split(" ")))
    print("Lonely Elements:", end=" ")
    answer = lonely_integer(integers)
    if answer:
        for element in answer:
            print(element, end=" ")
    else:
        print(None)

'''
OUTPUT:
Enter the numbers: 1 1 2 5 9 8 7 3 25 45 65 45 26 65 3 5 9 8 5 3 9
Lonely Elements: 2 7 25 26 
'''
