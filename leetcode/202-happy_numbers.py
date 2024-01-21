def is_happy(n):

    happy_map = {}

    while n != 1:
        if n not in happy_map:
            happy_map[n] = 1
        else:
            return False
        n_tmp = 0
        for digit in str(n):
            n_tmp += int(digit)**2
        n = n_tmp


    return True

print(is_happy(n = 19))
print(is_happy(n = 2))
print(is_happy(n = 2**31))