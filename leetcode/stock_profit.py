def print_it(func):
    def wrap(*args, **kwargs):
        print(func(*args, **kwargs))
        return func(*args, **kwargs)
    return wrap

@print_it
def calc_profit(prices):
    profits = []

    last_min, last_max = 10**9, 0
    for i, price in enumerate(prices):
        i_min = min(price, last_min)
        if i_min < last_min:
            profits.append(max(0, last_max - last_min))
            last_max = i_min
            last_min = i_min
        if price > last_max:
            last_max = max(price, last_max)
        else:
            profits.append(max(0, last_max - last_min))
            last_max = price
            last_min = price
    
    largest_profit = max(0, last_max - last_min)
    for profit in profits:
        largest_profit += profits
    
    return largest_profit

calc_profit([7,1,5,3,6,4])