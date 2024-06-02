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


def calculate(s):

    i = 0
    while i < len(s):
        if s[i] == ' ':
            s = s[:i] + s[i+1:]
        else:
            i += 1

    starts = []
    segments = []

    i = 0
    while i < len(s):
        char = s[i]
        if char == '(':
            starts.append(i)
        if char == ')':
            val = starts.pop(-1)
            segments.append(s[val+1:i])
            s = f"{s[:val]}x{len(segments)}{s[i+1:]}"
            i = val
        i += 1

    segments.append(s)

    # nums = list((range(10)))
    for idx, seg in enumerate(segments):
        lst = []
        prev = 0
        for i, char in enumerate(seg):
            if char in ['+', '-']:
                val = seg[prev:i]
                if not val:
                    continue
                if 'x' in val:
                    val = segments[int(val.split('x')[1])-1]
                    if seg[prev] == '-':
                        val *= -1
                lst.append(int(val))
                prev = i
        val = seg[prev:]
        if 'x' in val:
            val = segments[int(val.split('x')[1])-1]
            if seg[prev] == '-':
                val *= -1
        lst.append(int(val))
        segments[idx] = sum(lst)

    return segments[-1]

print(calculate(s = "1-(     -2)"))
print(calculate(s = "1 + 1"))
print(calculate(s = "(1+(4+5+2)-3)+(6+8)"))
print(calculate(s = " 2-1 + 2 "))