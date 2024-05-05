def findMinArrowShots(points):

    arrows, lower_bound = 0, -2**33
    for r_min, r_max in sorted(points):
        if lower_bound < r_min:
            lower_bound = r_max
            arrows += 1
        else:
            lower_bound = min(lower_bound, r_max)

    return arrows

print(findMinArrowShots([[1,3],[3,6],[4,6],[5,8],[9,10]]))
print(findMinArrowShots([[10,16],[2,8],[1,6],[7,12]]))
print(findMinArrowShots([[1,2],[3,4],[5,6],[7,8]]))
print(findMinArrowShots([[1,2],[2,3],[3,4],[4,5]]))