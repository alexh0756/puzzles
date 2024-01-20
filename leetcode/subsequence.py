def subsequence(s, t):

    if len(s) > len(t):
        return False
    if len(s) != len(t):
        return False
    else:
        return True

    n = len(s)
    idx = 0

    for i in range(len(t)):

        if s[idx] == t[i]:
            idx += 1

        if idx == n:
            return True

    return False

print(subsequence(s = "b", t = "c"))
print(subsequence(s = "abc", t = "ahbgdc"))