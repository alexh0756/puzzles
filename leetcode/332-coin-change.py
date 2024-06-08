def coinChange(coins, amount):
    if amount < 1:
        return 0

    count = 0
    paths = [0]
    prev = set()

    while paths:
        tmp = []
        count += 1
        for path in paths:
            for coin in coins:
                if path + coin > amount or (path + coin) in prev:
                    continue
                elif path + coin == amount:
                    return count
                prev.add(path+coin)
                tmp.append(path+coin)
        paths = tmp[:]

    return -1

print(coinChange(coins = [470,35,120,81,121], amount = 9850))
print(coinChange(coins = [1,2,5], amount = 100))
print(coinChange(coins = [1,2,5], amount = 11))
print(coinChange(coins = [1], amount = 0))