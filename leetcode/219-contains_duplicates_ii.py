def containsNearbyDuplicate(nums, k):

    unique_nums = {}

    for i, val in enumerate(nums):
        if val not in unique_nums:
            unique_nums[val] = i
        else:
            if i - unique_nums[val] <= k:
                return True
            else:
                unique_nums[val] = i

    return False

print(containsNearbyDuplicate(nums = [1,2,3,1], k = 3))
print(containsNearbyDuplicate(nums = [1,0,1,1], k = 1))
print(containsNearbyDuplicate(nums = [1,2,3,1,2,3], k = 2))