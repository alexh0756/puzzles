def findMinArrowShots(points):

    points.sort()
    map_nums = {-1: []}

    i = 0
    while i < len(points):
        if len(points) == 1:
            map_nums[-1].append(points[i])
            points.pop(i)
        elif points[i][1] < points[i+1][0]:
            map_nums[-1].append(points[i])
            points.pop(i)
        else:
            for val in range(points[i+1][0], points[i][1]+1):
                if val not in map_nums:
                    map_nums.update({val: [points[i], points[i+1]]})
                else:
                    for rge in [points[i], points[i+1]]:
                        if rge in map_nums[i]:
                            continue
                        else:
                            map_nums[i].append(rge)
            points.pop(i)

    unique_combos = {}
    for k, v in map_nums.items():
        if not v:
            continue
        tup_val = tuple(map(tuple, v))
        if tup_val not in unique_combos.keys():
            unique_combos.update({tup_val: {'i': k, 'len': len(v)}})

    darts = len(unique_combos)

    return darts

print(findMinArrowShots([[10,16],[2,8],[1,6],[7,12]]))
print(findMinArrowShots([[1,2],[3,4],[5,6],[7,8]]))
print(findMinArrowShots([[1,2],[2,3],[3,4],[4,5]]))