def numSteps(s):

    count = 0
    s = list(s)

    while len(s) > 1:
        i = len(s) - 1

        rem = s[i]
        count += int(rem)
        while rem == '1':
            if i < 0:
                s.insert(0, '1')
                break
            elif s[i] == '0':
                s[i] = rem
                rem = '0'
            else:
                s[i] = '0'
                rem = '1'

            i -= 1

        s = s[:len(s)-1]
        count += 1

    return i


print(numSteps(s = "1101"))
print(numSteps(s = "1111011110000011100000110001011011110010111001010111110001"))
print(numSteps(s = "10"))
print(numSteps(s = "1"))