from collections import Counter

def singleNumber(nums):
    counts = Counter(nums)
    for k, v in counts.items():
        if v == 1:
            return k
    return -1

print(singleNumber(nums = [2,2,3,2]))
print(singleNumber(nums = [0,1,0,1,0,1,99]))