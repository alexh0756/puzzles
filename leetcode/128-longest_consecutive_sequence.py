def longestConsecutive(nums):

    if len(nums) in (0, 1):
        return len(nums)

    nums.sort()

    counter = 1
    previous = nums[0]
    max_seq = 0
    for num in nums[1:]:
        if num == previous + 1:
            counter += 1
        elif num == previous:
            continue
        else:
            max_seq = max(counter, max_seq)
            counter = 1
        previous = num

    max_seq = max(counter, max_seq)
    
    return max_seq

print(longestConsecutive(nums = [100,4,200,1,3,2]))
print(longestConsecutive(nums = [0,3,7,2,5,8,4,6,0,1]))