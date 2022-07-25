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

# Comments in Python
A high sign (#) that is not inside a string literal begins a comment. All characters after the # and up to the end of the physical line are part of the comment and the Python interpreter ignores them.
```md
# First comment
print("Hello, Python!") # second comment
```
This produces like following result - 
```md
Hello, Python!
```
You can type a comment on the same line after a statement or expression -
```md
name = "Anuj Bisht" # This is a comment
```
You can comment multiple lines as follows - 
```md
# This is a comment.
# This is a comment, too.
```
Following triple-quoted string is also ignored by Python interpreter and can be used as a mutiline comments:
```md
'''
This is a multiline
comment.
'''
```

# Using Blank Lines
A line containing only whitespace, possibly with a comment, is known as a blank line and Python totally ignores it. In an interactive interpreter session, you must enter an empty physical line to terminate a multiline statement.

# Waiting for the user
The following lone of the program displays the prompt, the statement saying, "Press the enter key to exit", and waits for the user to take the action - 
```md
input("nnPress the enter key to exit.")
```
Here, <b> "nn"  </b> is used to create two new lines before displaying the actual line. Once the user presses the key, the program ends. This is a nice trick to keep a console window open until the user is done with an application.

# Multiple Statements on a Single Line
The semicolon (;) allows multiple statements on the single line given that neither statement starts a new code block. Here is a new code block. Here is a sample snip using the semicolon -
```md
import sys; x = 'foo'; sys.stdout.write(x + 'n')
```
