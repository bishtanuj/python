# Data Types in Python
> In computer science, a data type or simply type is an attribute of data which tells the compiler or interpreter how the programmer intend to use the data.
<br><br>

Python has the following built-in data types <br>
| Data Type | |
| :---: | :---: |
| Text Type | `str` |
| Numeric Type | `int`, `float`, `complex` |
| Sequence Type | `list`, `tuple`, `range` |
| Mapping Type | `dict` |
| Set Type | `set`, `frozenset` |
| Boolean | `bool` |
| Binary Type | `bytes`, `bytearray`, `memoryview` |
| None Type | `NoneType` |

<img style="width:50%; display:block; margin-left:auto; margin-right:auto;" src="https://upload.wikimedia.org/wikipedia/commons/thumb/1/10/Python_3._The_standard_type_hierarchy.png/636px-Python_3._The_standard_type_hierarchy.png"> 

# Python Numbers
Number data types store numeric values. Number objects are created when you assign a value to them. For example:
```md
num1 = 100
num2 = 200.222
```
Python supports four different numerical types: <br>
* int (signed integers) <br>
* long (long integers, they can also be represented in octal and hexadecimal) <br>
* float (floating point real values) <br>
* complex (complex numbers)

## Examples:
Here are some examples of numbers: <br>
| INT | LONG | FLOAT | COMPLEX |
| :---: | :---: | :---: | :---: |
| 10 | 51924361L | 0.0 | 3.14j |
| 100 | -0x19323L | 15.20 | 45.j |
| -786 | 0122L | -21.9 | 9.322e-36j |
| 080 | 0xDEFABCECBDAECBFBAEI | 32.3+e18 | .876j |
| -0490 | 535633629843L | -90. | -.6545+0J |
| -0x260 | -4721885298529L | 70.2-E12 | 4.53e-7j |

Python allows you to use lowercase l with long, but it is recommended that you use only an uppercase L to avoid confusion with number 1. Python displays long integers with an uppercase L. <br>
A complex number consists of an ordered pair of real floating-point number denoted by x + yj, where x and y are the real number and j is the imaginary unit.

# Python Strings
Strings in Python are defined as a contiguous set of characters represented in the quotation marks. Python allows for either pairs of single or double quotes. Subsets of strings can be taken using the slice operator ([] and [:]) with indexes starting at 0 in the beginning of the string and working their way from -1 at the end. <br>
The plus (+) sign is the string concatenation operator and the asterisk (*) is the repetition operator. For example:
```md
str = 'Hello World!'
print(str)  # Prints complete string
print(str[0]) # Prints first character of the string
```
