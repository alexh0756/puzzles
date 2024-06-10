import numpy as np

def maxProfit(prices):
    length = len(prices)
    array = [[0]*length for i in range(length)]
    for i in range(length):
        array[i][i] = 0
    for i in range(length):
        for j in range(i+1, length):
            array[i][j] = prices[j] - prices[i]

    profit = 0
    for x in range(length-1, -1, -1):
        maxx = 0
        for y in range(length-1, -1, -1):
            if array[y][x] <= maxx:
                continue
            maxx = array[y][x]
            for i in range(y-1):
                profit = max(profit, maxx + max(array[i][:y+1]))

    return profit


def maxProfit(prices):
    if not prices:
        return 0

    buy1, buy2 = float('inf'), float('inf')
    sell1, sell2 = 0, 0

    for price in prices:
        buy1 = min(buy1, price)
        sell1 = max(sell1, price - buy1)
        
        buy2 = min(buy2, price - sell1)
        sell2 = max(sell2, price - buy2)

    return sell2
np.random.seed(1)
print(maxProfit(prices = np.random.randint(1, 1000, 10000)))
print(maxProfit(prices = [3,3,5,0,0,3,1,4]))
print(maxProfit(prices = [3,3,5,0,0,3,1]))
print(maxProfit(prices = [7,6,4,3,1]))
print(maxProfit(prices = [1,2,3,4,5]))