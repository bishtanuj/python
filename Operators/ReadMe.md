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
| **S. No.** | **Operators** | **Name** | **Example** | **Program** |
| :---: | :---: | :---: | :---: | :---: |
| 1. | + | Addition | a + b | [addition.py](https://github.com/bishtanuj/python/blob/main/Operators/Programs/addition.py) |
| 2. | - | Subtraction | a - b | [subtraction.py](https://github.com/bishtanuj/python/blob/main/Operators/Programs/subtraction.py) |
| 3. | * | Multiplication | a * b | [multiplication.py](https://github.com/bishtanuj/python/blob/main/Operators/Programs/multiplication.py) |
| 4. | / | Division | a / b | [division.py](https://github.com/bishtanuj/python/blob/main/Operators/Programs/division.py) |
| 5. | // | Floor Division | a // b | [floor_division.py](https://github.com/bishtanuj/python/blob/main/Operators/Programs/floor_division.py) |
| 6. | % | Modulus | a % b | [modulus.py](https://github.com/bishtanuj/python/blob/main/Operators/Programs/modulus.py) |
| 7. | ** | Exponentiation | a ** b | [exponentation.py](https://github.com/bishtanuj/python/blob/main/Operators/Programs/exponentation.py) |


## Assignment Operators
**An assignment operator is the operator used to assign a new value to a variable.** <br>
| **S. No.** | **Operators** | **Example** | **Same As** | **Program** |
| :---: | :---: | :---: | :---: | :---: |
| 1. | = | a = 0 | a = 0 | [assignment_op_1.py](https://github.com/bishtanuj/python/blob/main/Operators/Programs/assignment_op_1.py) |
| 2. | += | a += 5 | a = a + 5 | [assignment_op_2.py](https://github.com/bishtanuj/python/blob/main/Operators/Programs/assignment_op_2.py) |
| 3. | -= | a -= 5 | a = a - 5 | [assignment_op_3.py](https://github.com/bishtanuj/python/blob/main/Operators/Programs/assignment_op_3.py) |
| 4. | *= | a *= 5 | a = a * 5 | [assignment_op_4.py](https://github.com/bishtanuj/python/blob/main/Operators/Programs/assignment_op_4.py) | 
| 5. | /= | a /= 5 | a = a / 5 | [assignment_op_5.py](https://github.com/bishtanuj/python/blob/main/Operators/Programs/assignment_op_5.py) |
| 6. | %= | a %= 5 | a = a % 5 | [assignment_op_6.py](https://github.com/bishtanuj/python/blob/main/Operators/Programs/assignment_op_6.py) |
| 7. | //= | a //= 5 | a = a // 5 | [assignment_op_7.py](https://github.com/bishtanuj/python/blob/main/Operators/Programs/assignment_op_7.py) |
| 8. | **= | a **= 5 | a = a ** 5 | [assignment_op_8.py](https://github.com/bishtanuj/python/blob/main/Operators/Programs/assignment_op_8.py) |
| 9. | l= | a l= 5 | a = a l 5 | [assignment_op_9.py](https://github.com/bishtanuj/python/blob/main/Operators/Programs/assignment_op_9.py) |
| 10. | &= | a &= 5 | a = a & 5 | [assignment_op_10.py](https://github.com/bishtanuj/python/blob/main/Operators/Programs/assignment_op_10.py) |
| 11. | ^= | a ^= 5 | a = a ^ 5 | [assignment_op_11.py](https://github.com/bishtanuj/python/blob/main/Operators/Programs/assignment_op_11.py) |
| 12. | >>= | a >>= 5 | a = a >> 5 | [assignment_op_12.py](https://github.com/bishtanuj/python/blob/main/Operators/Programs/assignment_op_12.py) |
| 13. | <<= | a <<= 5 | a = a << 5 | [assignment_op_13.py](https://github.com/bishtanuj/python/blob/main/Operators/Programs/assignment_op_13.py) |


## Comparison Operators
**Comparison operators can compare numbers or strings and perform evaluations. Expressions that use comparison operators do not return a number value as do arithmetic expressions. Comparison expressions returns either 1, which represents true or 0, which represents false.** <br>
| **S. No.** | **Operator** | **Name** | **Example** | **Program** |
| :---: | :---: | :---: | :---: | :---: |
| 1. | == | Equal | a == b | [comparison_op_1.py](https://github.com/bishtanuj/python/blob/main/Operators/Programs/comparison_op_1.py) |
| 2. | != | Not Equal | a != b | [comparison_op_2.py](https://github.com/bishtanuj/python/blob/main/Operators/Programs/comparison_op_2.py) |
| 3. | > | Greater Than | a > b | [comparison_op_3.py](https://github.com/bishtanuj/python/blob/main/Operators/Programs/comparison_op_3.py) |
| 4. | < | Less Than | a < b | [comparison_op_4.py](https://github.com/bishtanuj/python/blob/main/Operators/Programs/comparison_op_4.py) |
| 5. | >= | Greater Than or Equal To | a >= b | [comparison_op_5.py](https://github.com/bishtanuj/python/blob/main/Operators/Programs/comparison_op_5.py) |
| 6. | <= | Less Than or Equal To | a <= b | [comparison_op_6.py](https://github.com/bishtanuj/python/blob/main/Operators/Programs/comparison_op_6.py) |


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
