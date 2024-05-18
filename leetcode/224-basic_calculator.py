def calculate(s):

    i = 0
    while i < len(s):
        if s[i] == ' ':
            s = s[:i] + s[i+1:]
        else:
            i += 1

    i = 0
    while i < len(s):
        if s[i] not in ('+', '-'):
            i += 1
            continue
        
        if s[i] == '+':
            val = int(s[i-1]) + int(s[i+1])
        elif s[i] == '-':
            val = int(s[i-1]) - int(s[i+1])

        s = s[:i-1] + str(val) + s[i+2:]

    return s

print(calculate(s = "1 + 1"))
print(calculate(s = " 2-1 + 2 "))
print(calculate(s = "(1+(4+5+2)-3)+(6+8)"))