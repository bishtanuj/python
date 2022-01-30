""" 
Write a Python program which accepts the radius of a circle from the user and compute the area.
"""

from math import pi
radius = float(input("Enter the radius of circle: "))
area = pi * radius**2
print("Area of circle: ",area)
