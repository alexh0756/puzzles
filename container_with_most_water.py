def max_area(height):

    n = len(height) - 1
    i = 0
    total_water = 0

    storage = {}
    for i, num in enumerate(height):
        storage.update({num: [i]})

    height.sort(reverse=True)

    return

print(max_area([1, 8, 6, 2, 5, 4, 8, 3, 7]))
print(max_area([1, 1]))