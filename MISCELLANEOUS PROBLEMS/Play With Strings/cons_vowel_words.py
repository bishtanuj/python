# Program to count the number of words, consonants and vowels in a string

string = input("Enter the string: ")
length_string = len(string)
count_vowel, count_cons, count_words = 0, 0, 0
for i in range(length_string):
    if string[i] in ['a','e','i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']:
        count_vowel += 1
    elif string[i] == " ":
        count_words += 1
    else:
        count_cons += 1

print(f"Total number of words: {count_words + 1}")
print(f"Total number of vowel: {count_vowel}")
print(f"Total number of consonants: {count_cons}")
