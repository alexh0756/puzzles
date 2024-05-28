def equalSubstring(s, t, maxCost):

    lst = []
    for i in range(len(s)):
        lst.append(abs(ord(s[i]) - ord(t[i])))

    i, j = 0, 0
    running_sum = 0
    max_len = 0
    while i < len(s) and j < len(s):
        while j < len(s) and running_sum + lst[j] <= maxCost:
            running_sum += lst[j]
            j += 1

        max_len = max(max_len, j - i)
        running_sum -= lst[i]
        i += 1

        
    return max_len

print(equalSubstring(s = "krpgjbjjznpzdfy", t = "nxargkbydxmsgby", maxCost=14))
print(equalSubstring(s = "abcd", t = "bcdf", maxCost = 3))
print(equalSubstring(s = "abcd", t = "cdef", maxCost = 3))
print(equalSubstring(s = "abcd", t = "acde", maxCost = 0))