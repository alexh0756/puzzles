def permute(nums):
    if not nums:
        return [[]]
    
    lst = []
    for i, num in enumerate(nums):
        tmp = []
        
        for i in permute(nums[:i] + nums[i+1:]):
            tmp.append([num] + i)
        lst.extend(tmp)

    return lst


print(permute(nums = [1, 2, 3]))
print(permute(nums = [0, 1]))
print(permute(nums = [1]))