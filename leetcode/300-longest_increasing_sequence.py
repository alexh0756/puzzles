def lengthOfLIS(nums):

    vec = [1]*len(nums)

    for i in range(len(nums)-1):
        vec[i+1] = 1 + (vec[i] * int(nums[i] < nums[i+1]))

    return max(vec)


def lengthOfLIS(nums):
    
    store = {}
    last = {}

    for num in nums:
        for k in store.keys():
            if num > last[k]:
                store[k] += 1
                last[k] = num
        if num not in store:
            store[num] = 1
            last[num] = num

    return max(store.values())


def lengthOfLIS(nums):
    
    if not nums:
        return 0
    
    n = len(nums)
    dp = [1] * n

    for i in range(1, n):
        for j in range(i):
            if nums[i] > nums[j]:
                dp[i] = max(dp[i], dp[j] + 1)

    return max(dp)

print(lengthOfLIS(nums = [10,9,2,5,3,7,101,18]))
print(lengthOfLIS(nums = [0,1,0,3,2,3]))
print(lengthOfLIS(nums = [7,7,7,7,7,7,7]))