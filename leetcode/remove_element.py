def remove_element(nums, val):

    count, i = 0, len(nums) - 1
    while i > -1:
        if nums[i] == val:
            count += 1
            nums.pop(i)
            nums.append(None)
        i -= 1

    return count, nums

print(remove_element(nums = [3,2,2,3], val = 3))
print(remove_element(nums = [0,1,2,2,3,0,4,2], val = 2))