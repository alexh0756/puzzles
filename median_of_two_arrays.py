def findMedianSortedArrays(nums1, nums2) -> float:

    n = len(nums1) + len(nums2)
    length = 2 if n % 2 == 0 else 1
    medians = []
    middle = (n - 1) / 2
    i, j = 0, 0

    while len(medians) < length:

        if (nums1[i] < nums2[j] and i + 1 < len(nums1)) or (j + 1 == len(nums2)):
            if middle - 0.5 <= i + j <= middle + 0.5:
                medians.append(min(nums1[i], nums2[j]))
            i += 1
        elif (nums1[i] > nums2[j] and j + 1 < len(nums1)) or (i + 1 == len(nums1)):
            if middle - 0.5 <= i + j <= middle + 0.5:
                medians.append(min(nums1[i], nums2[j]))
            j += 1
        elif i + 1 < len(nums1):
            i += 1
        else:
            j += 1
        
    if len(medians) == 1:
        return medians[0]
    else:
        return sum(medians) / len(medians)

print(findMedianSortedArrays(nums1 = [1,3], nums2 = [2]))
print(findMedianSortedArrays(nums1 = [1,2], nums2 = [3,4]))