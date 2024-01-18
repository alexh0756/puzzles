def findMedianSortedArrays(nums1, nums2) -> float:

    n = len(nums1) + len(nums2)
    length = 2 if n % 2 == 0 else 1
    medians = []
    middle = (n - 1) / 2
    i, j = 0, 0

    while len(medians) < length:
        n1 = nums1[i] if i < len(nums1) else 10**7
        n2 = nums2[j] if j < len(nums2) else 10**7

        if middle - 0.5 <= i + j <= middle + 0.5:
            medians.append(min(n1, n2))

        if n1 < n2:
            i += 1
        elif n2 < n1:
            j += 1
        elif i < len(nums1):
            i += 1
        else:
            j += 1
        
    if len(medians) == 1:
        return medians[0]
    else:
        return sum(medians) / len(medians)

print(findMedianSortedArrays(nums1 = [0, 0], nums2 = [0, 0]))
print(findMedianSortedArrays(nums1 = [1,3], nums2 = [2]))
print(findMedianSortedArrays(nums1 = [1,2], nums2 = [3,4]))