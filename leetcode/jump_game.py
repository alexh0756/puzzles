def print_it(func):
    def wrap(*args, **kwargs):
        result = func(*args, **kwargs)
        print(result)
        return result
    return wrap

# @print_it
def canJump(nums) -> bool:
    # def depth_first_search(nums):
        
    if len(nums) == 1:
        return True
    if nums[0] == 0:
        return False

    i = min(len(nums) - 1, nums[0])
    while i > 0:
        result = canJump(nums[i:])
        i -= 1
        if result:
            break
    return result


def canJump(nums) -> bool:
    # def depth_first_search(nums):

    jump = 0
    reachable = 0
    max_tmp = 1

    while max_tmp > 0:
        max_tmp = 0
        for j in range(reachable - jump, reachable + 1):
            max_tmp = max(max_tmp, nums[j] + j - reachable)
        jump = max_tmp - 1
        reachable += max_tmp

        if reachable >= len(nums) - 1:
            return True

    return False

def canJump(nums) -> bool:
    # def depth_first_search(nums):

    jump = 0
    reachable = 0
    max_tmp = 1
    counter = 0

    while max_tmp > 0:
        max_tmp = 0
        for j in range(reachable - jump, reachable + 1):
            max_tmp = max(max_tmp, nums[j] + j - reachable)
        jump = max_tmp - 1
        reachable += max_tmp
        counter += 1

        if reachable >= len(nums) - 1:
            return counter

    return counter

canJump([0])
canJump([3,2,1,0,4])
canJump([2,3,1,1,4])
canJump([2,0,6,9,8,4,5,0,8,9,1,2,9,6,8,8,0,6,3,1,2,2,1,2,6,5,3,1,2,2,6,4,2,4,3,0,0,0,3,8,2,4,0,1,2,0,1,4,6,5,8,0,7,9,3,4,6,6,5,8,9,3,4,3,7,0,4,9,0,9,8,4,3,0,7,7,1,9,1,9,4,9,0,1,9,5,7,7,1,5,8,2,8,2,6,8,2,2,7,5,1,7,9,6])
canJump([2,0,0])
canJump([3,2,1,0,4])