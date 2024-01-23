def summaryRange(nums):

    if not nums:
        return []
        
    ranges = []
    prev_vals = []

    for i, val in enumerate(nums):
        if not prev_vals:
            prev_vals = [val]
            continue
        if prev_vals[-1] + 1 == val:
            prev_vals.append(val)
        else:
            if len(prev_vals) > 1:
                ranges.append(f"{prev_vals[0]}->{prev_vals[-1]}")
            else:
                ranges.append(prev_vals[0])
            prev_vals = [val]

    if len(prev_vals) > 1:
        ranges.append(f"{prev_vals[0]}->{prev_vals[-1]}")
    else:
        ranges.append(f"{prev_vals[0]}")


    return ranges

print(summaryRange([0,1,2,4,5,7]))
print(summaryRange([0,2,3,4,6,8,9]))