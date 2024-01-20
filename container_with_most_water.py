def max_area(height):

    water = 0
    i, j = 0, len(height) - 1

    while i < j:

        val_cur = min(height[j], height[i]) * (j - i)

        water = max(water, val_cur)
        if height[i] < height[j]:
            i += 1
        elif height[i] > height[j]:
            j -= 1
        else:
            i += 1
            j -= 1

    return water

print(max_area([1,8,100,2,100,4,8,3,7]))
print(max_area([1,8,6,2,5,4,8,25,7]))
print(max_area([1, 2, 4, 3]))
print(max_area([1, 2, 1]))
print(max_area([1, 8, 6, 2, 5, 4, 8, 3, 7]))
print(max_area([1, 1]))
print(max_area([10**3]*10**5))