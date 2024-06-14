def minIncrementForUnique(nums):

    nums = sorted(nums)

    tmp = []
    count = 0
    i = 1
    while i < len(nums):

        if tmp and i < len(nums) - 1 and nums[i]+1 < nums[i+1]:
            count += nums[i] - tmp.pop(0)
            nums.insert(i+1, nums[i]+1)
        if nums[i] <= nums[i-1]:
            tmp.append(nums.pop(i))
            i -= 1
        else:
            i += 1

    for i, num in enumerate(tmp):
        count += nums[-1] - num + i + 1

    return count


print(minIncrementForUnique(nums=[0, 2, 0]))
print(minIncrementForUnique(nums=[3, 2, 1, 2, 1, 7]))
print(minIncrementForUnique(nums=[2, 2, 2, 2, 0]))
print(minIncrementForUnique(nums=[1, 2, 2, 2]))
print(minIncrementForUnique(nums=[0, 0]))
print(minIncrementForUnique(nums=[1, 2, 2]))
