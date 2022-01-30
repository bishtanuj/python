"""
Write a Python program to accept a filename from the user and print the extension of that.
Sample filename : abc.java
Output : java
"""

file_name = input("Enter the name of the file: ")
file_extension = file_name.split(".")
print("The extension of file: " + repr(file_extension[-1]))
