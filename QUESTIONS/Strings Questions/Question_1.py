# Program to count the frequency of elements in the string

def count_frequency(str1):
    dictionary = {}
    for i in str1:
        keys = dictionary.keys()
        if i in keys:
            dictionary[i] += 1
        else:
            dictionary[i] = 1

    print("The frequency of the elements in given string:")
    print(dictionary)


if __name__ == '__main__':
    string = input("Enter a string: ")
    count_frequency(string)

    
# Output Sample
# Enter a string: Hi, how are you?
# The frequency of the elements in given string:
# {'H': 1, 'i': 1, ',': 1, ' ': 3, 'h': 1, 'o': 2, 'w': 1, 'a': 1, 'r': 1, 'e': 1, 'y': 1, 'u': 1, '?': 1}
