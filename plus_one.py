def plus_one(digits):

    i = len(digits) - 1
    carry = 1

    while carry != 0 and i > -1:
        val = (digits[i] + 1)
        digits[i] = val % 10
        carry = val // 10
        i -= 1

    if i == -1 and carry != 0:
        digits.insert(0, carry)

    return digits

print(plus_one([9, 9, 9, 9, 9]))
print(plus_one([9]))
print(plus_one([1, 2, 3]))
print(plus_one([4, 3, 2, 1]))