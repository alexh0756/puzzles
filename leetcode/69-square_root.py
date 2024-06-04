def mySqrt(n):
    
    for i in range(46_500):
        if i**2 > n:
            return i - 1

    return -1


def mySqrt(x):
    
    l = 0
    r = x
    while l <= r:
        m = (l+r)//2
        if m*m == x:
            return m
        elif m*m < x:
            l = m + 1
        else:
            r = m - 1

    return r

print(mySqrt(100))
print(mySqrt(1073741824))
print(mySqrt(4))
print(mySqrt(8))