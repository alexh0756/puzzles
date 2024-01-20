def is_palindrone(x):

    x = str(x)

    for i in range(len(x) // 2):
        if x[i] != x[-1-i]:
            return False

    return True

print(is_palindrone(x = 1))
print(is_palindrone(x = 121))
print(is_palindrone(x = -121))
print(is_palindrone(x = 10))