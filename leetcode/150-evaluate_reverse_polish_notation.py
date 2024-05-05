def evalRPN(tokens):

    i = 0
    while len(tokens) > 1:
        
        if tokens[i] not in ('+', '-', '*', '/'):
            i += 1
            continue
        elif tokens[i] in ('+'):
            val = int(tokens[i-2]) + int(tokens[i-1])
        elif tokens[i] in ('-'):
            val = int(tokens[i-2]) - int(tokens[i-1])
        elif tokens[i] in ('/'):
            val = int(tokens[i-2]) / int(tokens[i-1])
            val = str(val).split('.')[0]
        elif tokens[i] in ('*'):
            val = int(tokens[i-2]) * int(tokens[i-1])
        
        tokens[i-2] = str(val)
        tokens.pop(i-1)
        tokens.pop(i-1)
        i -= 2

    return int(tokens[0])

print(evalRPN(tokens = ["2","1","+","3","*"]))
print(evalRPN(tokens = ["4","13","5","/","+"]))
print(evalRPN(tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]))