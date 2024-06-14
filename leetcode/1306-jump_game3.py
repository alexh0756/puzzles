def canReach(arr, start):

    seen = {start}
    next = [start]

    while next:
        pos = next.pop(0)
        for dir in [1, -1]:
            option = pos+(arr[pos]*dir)
            if 0 < option < len(arr) and option not in seen:
                if arr[option] == 0:
                    return True
                next.append(option)
                seen.add(option)
    return False


print(canReach(arr=[0, 1], start=1))
print(canReach(arr=[4, 2, 3, 0, 3, 1, 2], start=5))
print(canReach(arr=[4, 2, 3, 0, 3, 1, 2], start=0))
print(canReach(arr=[3, 0, 2, 1, 2], start=2))
