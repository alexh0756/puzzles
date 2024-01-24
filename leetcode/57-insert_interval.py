def insert_interval(intervals, newInterval):

    if not intervals:
        return [newInterval]

    overlapping = []
    insert_i = len(intervals) + 1
    start, end = newInterval[0], newInterval[1]

    for i, lst in enumerate(intervals):
        if (start <= lst[0] and lst[0] <= end) or (start <= lst[1] and lst[1] <= end) or (lst[0] <= start and end <= lst[1]):
            overlapping.append(i)
            insert_i = min(insert_i, i)
            start = min(start, lst[0])
            end = max(end, lst[1])
        elif i < len(intervals) - 1 and (lst[1] < start and end < intervals[i+1][0]):
            insert_i = i + 1

    for i in overlapping:
        intervals.pop(overlapping[0])
    if insert_i < len(intervals) + 1:
        intervals.insert(insert_i, [start, end])
    elif end <= intervals[0][0]:
        intervals.insert(0, [start, end])
    elif intervals[-1][1] <= start:
        intervals.append([start, end])

    return intervals

print(insert_interval(intervals = [[1,2], [8,9]], newInterval = [4,5]))
print(insert_interval(intervals = [[3,4]], newInterval = [1,2]))
print(insert_interval(intervals = [[1,3]], newInterval = [4,5]))
print(insert_interval(intervals = [[1,5]], newInterval = [2,3]))
print(insert_interval(intervals = [[1,3],[6,9]], newInterval = [2,5]))
print(insert_interval(intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]))