def is_valid(s):

    stack = []

    for char in s:
        if char in '([{':
            stack.append(char)
        elif char in '}])' and len(stack)==0:
            return False
        elif char == ')' and stack[-1] == '(':
            stack.pop(-1)
        elif char == ']' and stack[-1] == '[':
            stack.pop(-1)
        elif char == '}' and stack[-1] == '{':
            stack.pop(-1)
        else:
            return False

    if len(stack) == 0:
        return True
    else:
        return False

print(is_valid("()[]{}"))
print(is_valid("(]"))