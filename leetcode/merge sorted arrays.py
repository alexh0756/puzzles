def merge(nums1, m, nums2, n):
    nums1[m:m+n] = nums2
    while n > 0:
        i = m
        while i > 0:
            if nums1[i] < nums1[i-1]:
                nums1[i], nums1[i-1] = nums1[i-1], nums1[i]
                i -= 1
            else:
                break
        m += 1
        n -= 1
    print(nums1)
    return nums1

merge(nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3)
merge(nums1 = [0], m = 0, nums2 = [1], n = 1)
merge(nums1 = [1], m = 1, nums2 = [], n = 0)
