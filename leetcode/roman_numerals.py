def romanToInt(s: str) -> int:
    numerals = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }

    last = 'M'
    running_sum = 0
    for i in s:
        if (last in ('I', 'X', 'C')) and (numerals[i] / numerals[last] in (5, 10)):
            running_sum += numerals[i] - numerals[last] * 2
        elif numerals[i] <= numerals[last]:
            running_sum += numerals[i]
        else:
            running_sum = numerals[i] - running_sum
        last = i
        # print(running_sum, last)

    return running_sum

# print(romanToInt("III"), 3)
# print(romanToInt("LVIII"), 58)
# print(romanToInt("MCMXCIV"), 1994)


def intToRoman(num: int) -> str:
    numerals = {
        1 : 'I',
        5 : 'V',
        10 : 'X',
        50 : 'L',
        100 : 'C',
        500 : 'D',
        1000 : 'M',
        5000: ''
    }

    output = ''
    num = str(num)
    magnitute = len(num)
    for char in num:
        char = int(char)
        mag_calc = 10**(magnitute-1)
        if char in (4, 9):
            output += numerals[(char+1)*mag_calc/(char+1)] + numerals[(char+1)*mag_calc]
        else:
            singles = char % 5
            fives = char // 5
            output += numerals[5*mag_calc] * fives + numerals[mag_calc] * singles

        magnitute -= 1

    return 0

print(intToRoman(num = 3))
print(intToRoman(num = 58))
print(intToRoman(num = 1994))