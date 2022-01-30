""" 
Write a Python program to display the current date and time.
Sample Output :
Current date and time :
2022-01-30 14:34:14
"""

import datetime
current = datetime.datetime.now()
print("Current date and time: ")
print(current.strftime("%Y-%m-%d %H:%M:%S"))
