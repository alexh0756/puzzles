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

    left_max = {"idx": [-1, -1], "value": [-1, -1]}
    right_max = {"idx": [-1, -1], "value":[-1, -1]}

    for i, num in enumerate(height):
        print(i+num)
        if i + num >= right_max['idx'][0] + right_max['value'][0]:
            right_max['idx'] = [i, right_max['idx'][0]]
            right_max['value'] = [num, right_max['value'][0]]
        elif i + num >= right_max['idx'][1] + right_max['value'][1]:
            right_max['idx'][1] = i
            right_max['value'][1] = num
    print()
    for i, num in enumerate(height[:right_max['idx'][0]]):
        print(len(height) - i + num)
        if len(height) - i + num > len(height) - left_max['idx'][0] + left_max['value'][0]:
            left_max['idx'] = [i, left_max['idx'][0]]
            left_max['value'] = [num, left_max['value'][0]]
        elif len(height) - i + num > len(height) - left_max['idx'][1] + left_max['value'][1]:
            left_max['idx'][1] = i
            left_max['value'][1] = num

    # water = 0
    # if left_max['value'] > right_max['value']:
    #     for i in range(0, left_max['idx'] + 1):
    #         if (tmp := min(height[i], right_max['value']) * (right_max['idx'] - i)) > water:
    #             water = tmp
    # elif left_max['value'] < right_max['value']:
    #     for i in range(right_max['idx'], len(height)):
    #         if (tmp := min(left_max['value'], height[i]) * (i - left_max['idx'])) > water:
    #             water = tmp
    # else:
    water = 0
    for i in range(2):
        for j in range(2):
            tmp = min(left_max['value'][i], right_max['value'][j]) * (right_max["idx"][j] - left_max["idx"][i])
            if tmp > water:
                water = tmp

    return water

print(max_area([1,8,6,2,5,4,8,25,7]))
print(max_area([1, 2, 4, 3]))
print(max_area([1, 2, 1]))
print(max_area([1, 8, 6, 2, 5, 4, 8, 3, 7]))
print(max_area([1, 1]))
print(max_area([10**3]*10**5))