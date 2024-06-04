def hammingWeight(n):

    for i in range(31, -1, -1):
        count = 0
        val = 2**i
        if n - val >= 0:
            n -= val
            count += 1
        if n == 0:
            break

    return count