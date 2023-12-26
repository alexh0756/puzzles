def canCompleteCircuit(gas, cost) -> int:
    n = len(gas)
    diff = []
    search = {}

    for i in range(n):
        diff.append(gas[i] - cost[i])
        val = diff[i]
        if val > 0:
            if val not in search.keys():
                search.update({val: [i]})
            else:
                search[val].append(i)
        # if i > 0:
        #     diff[i] = diff[i-1] + diff[i]
    
    search_order = list(search.keys())
    search_order.sort(reverse=True)

    for search_k in search_order:
        for start in search[search_k]:
            possible = True
            i, value = start, 0
            while possible:
                value += diff[i]

                if value <= 0:
                    possible = False

                i = (i + 1) % n
                if i == start: 
                    return i
    
    return -1

    # print(diff)

    # for i in range(n):
    #     print()
    #     possible = True
    #     j = 0
    #     while possible and j < n:
    #         # if i != j:
    #         print(i, j, diff[j] + cost[i])
    #         if diff[j] + cost[i] < 0:
    #             possible = False
            
    #         j += 1
        
    #     if possible:
    #         return i

    return 0

canCompleteCircuit(gas = [4,5,3,1,4], cost = [5,4,3,4,2])
canCompleteCircuit(gas = [2,3,4], cost = [3,4,3])
canCompleteCircuit(gas = [1,2,3,4,5], cost = [3,4,5,1,2])