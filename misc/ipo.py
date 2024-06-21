import heapq

def findMaximizedCapital(k, w, profits, capital):

    store = {}
    queue = []
    
    for cap, prof in zip(capital, profits):
        if cap <= w:
            heapq.heappush(queue, (-prof, cap))
        elif cap not in store:
            store[cap] = [(-prof, cap)]
        else:
            store[cap].append((-prof, cap))

    total = w
    for project in range(k):
        prof, cap = heapq.heappop(queue)
        
        for k in [k for k in store.keys() if total < k <= total-prof]:
            lst = store.pop(k)
            for val in lst:
                heapq.heappush(queue, val)
        
        total += -prof

    return total

# print(findMaximizedCapital(k = 2, w = 0, profits = [1,2,3], capital = [0,1,1]))
print(findMaximizedCapital(k = 3, w = 0, profits = [1,2,3], capital = [0,1,2]))