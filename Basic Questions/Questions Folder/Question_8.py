# Write a program to check whether the input alphabet is vowel or consonant

alpha = inout("Enter an alphabet: ")

list_vowel = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']

if alpha in list_vowel:
    print(alpha, "is a vowel")
else:
    print(alpha, "is a consonant")


    
    
# Output
# Enter an alphabet: g
# g is a consonant

# # Output
# Enter an alphabet: E
# E is a vowel
