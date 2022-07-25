# Python Identifiers
A Python Identifiers is a name used to identify a variable, function, class, module or other object. An identifier starts with a letter A to Z or a to z or an underscore ( _ ) followed by zero or more letters, underscores and digits (0 to 9).
<br>
Python doesnot allow punctuation characters such as &commat, $, and % within identifiers. Python is a case sensitive programming language. Thus, Manpower and manpower are two different identifiers in Python.
<br>
Here are naming conventions for Python identifiers - <br>
* Class names with an upercase letter. All other identifiers start with the lowercase letter. <br>
* Starting an identifier with a single leading underscore indicates that the identifier is private. <br>
* Statrting an identifier with two leading underscores indicates a strongly private identifier. <br>
* If the identifier also ends with two trailing underscores, the identifier is a language - defined special name.

# Reserved Words
The following list shows the Python keywords. These are reserved words and you cannot use them as constant or variable or any other identifier names. All the Python keywords contain lowercase letters only. <br><br>
```md
1. and                                  11. exec                                  21. not          
2. assert                               12. finally                               22. or
3. break                                13. for                                   23. pass
4. class                                14. from                                  24. print
5. continue                             15. global                                25. raise
6. def                                  16. if                                    26. return
7. del                                  17. import                                27. try
8. elif                                 18. in                                    28. while
9. else                                 19. is                                    29. with
10. except                              20. lambda                                30. yield
```
# Lines and Indentation
Python provides no braces to indicate blocks of code for class and function definitions or flow control. Block of code are denoted by line indentation, which is rigidly enforced. <br>
The number of spaces in the indentation is variable, but all statements within the block must be indented in the same amount. For example - <br>
```md
if 10 > 5:
print("10 is greater than 5")
else:
print("10 is not greater than 5")
```
However, the following block generates an error - <br>
```md
if 10 > 5:
print("10 is greater than 5")
else:
print("10 is not greater than 5")
^
IndentationError: expected an indented block
```

# Multi - Line Statements
Statements in Python typically end with a new line. Python does, however, allow the use of the line continuation character () to denote that the line should continue. For example - <br>
```md
total = 5 +
10 +
30
print(total)
```
Statements contained within the [], {}, or () brackets do not need to use the line continuation character. For example - <br>
```md
months = ['Jan', 'Feb', 'March',
'Apr', 'May', 'Jun',
'Jul', 'Aug', 'Sept',
'Oct', 'Nov', 'Dec']
print(months)
```

# Quotation in Python
Python accepts single ('), double (") and triple (" or """) quotes to denote string literals, as long as the same type of quote starts and ends the string. <br>
The triple quotes are used to span the string across multiple lines. For example, all the following are legal - <br>
```md
word = 'word'
sentence = "This is a sentence."
paragraph = """This is a paragraph. It is
made up of multiple lines and sentences."""
```
