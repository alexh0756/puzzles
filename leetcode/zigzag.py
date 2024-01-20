def convert(s, numRows):
    if numRows == 1:
        return s

    stacks = ['' for _ in range(numRows)]

    direction = 1
    stack_idx = 0

    for char in s:

        stacks[stack_idx] += char
        
        stack_idx += direction
        if stack_idx in (0, numRows-1):
            direction *= -1

    string = ''
    for stack in stacks:
        string += stack

    return string


def convert_optimised(s, numRows):
    if numRows == 1:
        return s

    stacks = [''] * 3

    direction, stack_idx = 1, 0

    for char in s:

        stacks[stack_idx] += char
        
        stack_idx += direction
        if stack_idx in (0, numRows-1):
            direction *= -1

    return ''.join(stacks)

print(convert(s="PAYPALISHIRING", numRows=3))