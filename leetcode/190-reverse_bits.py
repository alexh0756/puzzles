def reverseBits(n: int) -> int:
    res = ''
    for i in range(31, -1, -1):
        val = (2**i)
        if n - val >= 0:
            n -= val
            res = '1' + res
        else:
            res = '0' + res

    return res


reverseBits(n = int('00000010100101000001111010011100', 2))