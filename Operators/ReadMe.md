# Python Operators

**In computer science, an operator is a character that determines the action that is to be performed or considered.**

Python divides the operators in the following groups:
* Arithmetic Operators
* Assignment Operators
* Comparison Operators
* Logical Operators
* Identity Operators
* Membership Operators
* Bitwise Operators


## Arithmetic Operators
**An arithmetic operators are used with numeric values to perform common mathematical opertations:** <br>
| **Operators** | **Name** | **Example** | **Program** |
| :---: | :---: | :---: | :---: |
| + | Addition | a + b | [addition.py](https://github.com/bishtanuj/python/blob/main/Operators/addition.py) |
| - | Subtraction | a - b | [subtraction.py](https://github.com/bishtanuj/python/blob/main/Operators/subtraction.py) |
| * | Multiplication | a * b | [multiplication.py](https://github.com/bishtanuj/python/blob/main/Operators/multiplication.py) |
| / | Division | a / b | [division.py](https://github.com/bishtanuj/python/blob/main/Operators/division.py) |
| // | Floor Division | a // b | [floor_division.py](https://github.com/bishtanuj/python/blob/main/Operators/floor_division.py) |
| % | Modulus | a % b | [modulus.py](https://github.com/bishtanuj/python/blob/main/Operators/modulus.py) |
| ** | Exponentiation | a ** b | [exponentation.py](https://github.com/bishtanuj/python/blob/main/Operators/exponentation.py) |


## Assignment Operators
**An assignment operator is the operator used to assign a new value to a variable.** <br>
| **S.No.** | **Operators** | **Example** | **Same As** | **Program** |
| :---: | :---: | :---: | :---: | :---: |
| 1. | = | a = 0 | a = 0 | |
| 2. | += | a += 5 | a = a + 5 | |
| 3. | -= | a -= 5 | a = a - 5 | |
| 4. | *= | a *= 5 | a = a * 5 | | 
| 5. | /= | a /= 5 | a = a / 5 | |
| 6. | %= | a %= 5 | a = a % 5 | |
| 7. | //= | a //= 5 | a = a // 5 | |
| 8. | **= | a **= 5 | a = a ** 5 | |
| 9. | &= | a &= 5 | a = a & 5 | |
| 10. | ^= | a ^= 5 | a = a ^ 5 | |
| 11. | >>= | a >>= 5 | a = a >> 5 | |
| 12. | <<= | a <<= 5 | a = a << 5 | |


## Comparison Operators
**Comparison operators can compare numbers or strings and perform evaluations. Expressions that use comparison operators do not return a number value as do arithmetic expressions. Comparison expressions returns either 1, which represents true or 0, which represents false.** <br>
| **Operator** | **Name** | **Example** | **Program** |
| :---: | :---: | :---: | :---: |
| == | Equal | a == b | |
| != | Not Equal | a != b | |
| > | Greater Than | a > b | |
| < | Less Than | a < b | |
| >= | Greater Than or Equal To | a >= b | |
| <= | Less Than or Equal To | a <= b | |


## Logical Operators
**Logical expressions, like comparisons expressions, return 1 (True) or 0 (False) when processed. Logical operators combine two comparisons and return 1 or 0 depending on the results of the comparisons.** <br>
| **Operators** | **Description** | **Example** | **Program** |
| :---: | :---: | :---: | :---: |
| and | Returns True if both statements are true | a < 5 and a < 10 | |
| or | Returns True if one of the statements is true | a < 5 or a == 5 | |
| not | Reverse the result, returns False if the result is true | not(a < 5 and a < 10) | |


## Identity Operators
**Identify operators are used to compare the objects, not if they are equal, but if they are actually the same object, with the same memory location.** <br>
| **Operators** | **Description** | **Example** | **Program** |
| :---: | :---: | :---: | :---: |
| is | Return True if both variables are the same object |a is b| |
| is not | Returns True if both variables are not same object | a is not b | |

## Membership Operators
**Membership operators are operators used to validate the membership of a value. It test for a membership in a sequence such as strings, lists or tuples.** <br>
| **Operators** | **Description** | **Example** | **Program** |
| :---: | :---: | :---: | :---: |
| in | Check if value exists in a sequence or not. Evaluates to true if it finds the variable in the specified sequence and false otherwise | a in b | |
| not in | Evaluates to true if it does not finds a variable in the specified sequence and false otherwise | a not in b | |


## Bitwise Operators
**Bitwise operators are operators used to compare (binary) numbers.**
| **Operators** | **Name** | **Description** | **Program** |
| :---: | :---: | :---: | :---: |
| & | AND | Sets each bit to 1 if both bits are 1 | |
| l | OR | Sets each bit to 1 if one of the two bits is 1 | |
| ^ | XOR | Sets each bit to 1 if only one of two bits is 1 | |
| ~ | NOT | Inverts all the bits | |
| << | Zero fill left shift | Shift left by pushing zeroes in form the right and let the leftmost bits fall of | |
| >> | Signed right shift | Shift right by pushing copies of the leftmost bit in from the left, and let the rightmost bits fall of | |
