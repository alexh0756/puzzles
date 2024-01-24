def merge(intervals):

    intervals.sort()
    overlapping = []
    start, end = intervals[0][0], intervals[0][1]
    for i in range(len(intervals)-1):
        if intervals[i+1][0] <= end:
            start = min(start, intervals[i+1][0])
            end = max(end, intervals[i+1][1])
        else:
            overlapping.append([start, end])
            start, end = intervals[i+1][0], intervals[i+1][1]

    overlapping.append([start, end])

    return overlapping

print(merge([[2,3],[4,5],[6,7],[8,9],[1,10]]))
print(merge([[1,4],[0,4]]))
print(merge([[1,3],[2,6],[8,10],[15,18]]))
print(merge([[1,4],[4,5]]))