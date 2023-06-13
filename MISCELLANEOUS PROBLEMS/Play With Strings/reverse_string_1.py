# Program to print the reverse of string without using inbuilt function

'''
Test Case:
INPUT: Hello
OUTPUT: olleH
'''

# function to reverse the string
def reverse_string(nums: list[str]) -> str:

    # let's create two pointers
    i, j = 0, len(nums) - 1

    # swap the elements to reverse the list
    while i <= j:
        nums[i], nums[j] = nums[j], nums[i]
        i += 1
        j -= 1

    # convert the list into string and return as an answer
    string_new = ""
    for element in nums:
        string_new += element
    return string_new


# driver function
if __name__ == '__main__':
    # scan the string
    string = input("Enter the string: ")

    # convert the string into list
    string_list = [i for i in string]

    # print the reverse string
    print(f"Reverse String: {reverse_string(string_list)}")
