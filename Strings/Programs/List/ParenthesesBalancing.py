# Program to check whether the parentheses are balanced in the string

# function to check parentheses balancing
def check_parentheses_balancing(exp: str) -> bool:
    stack = []
    for char in exp:
        if char in ['(', '{', '[']:
            stack.append(char)
        else:
            if not stack:
                return False
            current_char = stack.pop()
            if current_char == '(':
                if char != ')':
                    return False
            if current_char == '{':
                if char != '}':
                    return False
            if current_char == '[':
                if char != ']':
                    return False
    if stack:
        return False
    return True


if __name__ == '__main__':
    expression = input("Enter the expression: ")
    if check_parentheses_balancing(expression):
        print("The given expression is balanced")
    else:
        print("The given expression is not balanced")


'''
OUTPUT:
Enter the expression: {[()]}
The given expression is balanced
'''
