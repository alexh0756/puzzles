def myPow(x, n):

    if n == 0:
        return 1
    elif n < 0:
        return 1 / (x * myPow(x, -n - 1))
    elif n % 2 == 0:
        a = myPow(x, n // 2)
        return a * a
    return x * myPow(x, n - 1)

# print(myPow(0.00001, 2147483647))
print(myPow(2, 10))
print(myPow(2.1, 3))
print(myPow(2, -2))