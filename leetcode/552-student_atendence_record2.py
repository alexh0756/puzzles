from collections import Counter

def checkRecord_naive(n):

    if n == 0:
        return 0

    options = ['p', 'a', 'l']

    lst = options[:]
    for i in range(n-1):
        print(lst)
        tmp = []
        for l in lst:
            for option in options:
                entry = l + option
                if 'lll' in entry or Counter(entry)['a'] > 1:
                    continue
                tmp.append(entry)
        lst = tmp[:]
    print(lst)
    return len(lst)


def checkRecord(n):

    if n == 0:
        return 0

    counter = {'p': 1, 'a': 1, 'al':0, 'all':0, 'l':1, 'll':0}

    for i in range(n-1):
        prev = {k:v for k, v in counter.items()}
        counter['p'] = (prev['p'] + prev['l'] + prev['ll']) % (10**9 + 7)
        counter['a'] = (prev['p'] + prev['a'] + prev['l'] + prev['ll'] + prev['al'] + prev['all']) % (10**9 + 7)
        counter['l'] = (prev['p']) % (10**9 + 7)
        counter['al'] = (prev['a']) % (10**9 + 7)
        counter['ll'] = (prev['l']) % (10**9 + 7)
        counter['all'] = (prev['al']) % (10**9 + 7)

    return sum(counter.values()) % (10**9 + 7)

# print(checkRecord(n = 1))
# print(checkRecord(n = 2))
# print(checkRecord_naive(n = 3))
# print(checkRecord(n = 3))
# print(checkRecord(n = 4))
print(checkRecord(n = 10101))
print(checkRecord(n = 66666))
print(checkRecord(n = 98765))