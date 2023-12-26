def remove_duplicates(nums):
    i, length, last = 0, len(nums), -1
    while i < length:
        if last == nums[i]:
            nums.pop(i)
            length -= 1
        else:
            i += 1

        last = nums[i - 1]
    
    return length

remove_duplicates([1,1])
remove_duplicates([0,0,1,1,1,2,2,3,3,4])

def remove_duplicates_2(nums):
    i, length, last, counter = 0, len(nums), -101, 1
    while i < length:
        if last != nums[i]:
            i += 1
            counter = 1
        elif counter > 1:
            nums.pop(i)
            length -= 1
        else:
            counter += 1
            i += 1

        last = nums[i - 1]
    
    return length

remove_duplicates_2([1,1,1,2,2,3])
remove_duplicates_2([0,0,1,1,1,1,2,3,3])