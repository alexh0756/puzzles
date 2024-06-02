def combine(n, k):

    n_iter = 1
    nums = list(range(1, n+1))
    lst = [[num] for num in nums]

    while n_iter < k:
        tmp = []
        for each in lst:
            options = []
            for num in nums[each[-1]:]:
                options.append(each + [num])
            
            tmp.extend(options)
        lst = tmp[:]
        n_iter += 1

    return lst

print(combine(n = 4, k = 2))
print(combine(n = 1, k = 1))