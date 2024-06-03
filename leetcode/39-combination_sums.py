from collections import Counter

def combinationSum(candidates, target):

    lst = []
    for num in candidates:
        if num == target:
            lst.append([num])
        elif num < target:
            unique = []
            for cand in combinationSum(candidates, target-num):
                lst.append([num] + cand)
    
    lst = list(map(sorted, lst))
    i = 1
    while i < len(lst):
        if lst[i] in lst[i:]:
            lst.pop(i)
        else:
            i += 1

    return lst

print(combinationSum(candidates = [2,3,6,7], target = 7))