def max_area(height):

    n = len(height)
    total_water = 0
    max_height = {"idx":-1, "value":-1}

    for i in range(n):

        if i > max_height['idx']:
            for j in range(n - 1, i, -1):
                if height[j] > max_height['value']:
                    max_height = {"idx": j, "value": height[j]}


        for j in range(max_height['idx'], n):
            val = min(height[i], height[j]) * (j - i)
            if val > total_water:
                total_water = val

    return total_water

def max_area(height):

    left_max, right_max = {"idx":-1, "value":-1}, {"idx":-1, "value":-1}

    for i, num in enumerate(height):
        if i + num >= right_max['idx'] + right_max['value']:
            right_max = {"idx": i, "value": num}
    
        if len(height) - i + num > len(height) - left_max['idx'] + left_max['value']:
            left_max = {"idx": i, "value": num}

    return min(left_max['value'], right_max['value']) * (right_max["idx"] - left_max["idx"])

print(max_area([1, 2, 4, 3]))
print(max_area([1, 2, 1]))
print(max_area([1, 8, 6, 2, 5, 4, 8, 3, 7]))
print(max_area([1, 1]))
print(max_area([10**3]*10**5))