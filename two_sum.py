def two_sum(numbers, target):

    i, j = 0, len(numbers) - 1

    while i < j:

        if numbers[i] + numbers[j] < target:
            i += 1
        elif numbers[i] + numbers[j] > target:
            j -= 1
        else:
            return [i+1, j+1]

    return []

print(two_sum(numbers = [3,24,50,79,88,150,345], target = 200))
print(two_sum(numbers = [2,7,11,15], target = 9))
print(two_sum(numbers = [2,3,4], target = 6))
print(two_sum(numbers = [-1,0], target = -1))