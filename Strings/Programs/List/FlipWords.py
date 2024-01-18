# Program to flip the words of the string and make them correct.

def flip_words(string: str) -> str:
    string_list = [i for i in string[::-1].split(" ")][::-1]
    answer = ""
    for i in string_list:
        answer += i + " "
    return answer


if __name__ == '__main__':
    sentence = input("Enter the string: ")
    print(f"Result: {flip_words(sentence)}")
