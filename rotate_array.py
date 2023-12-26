def rotate(nums, k) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    length = len(nums)
    final_val = nums[length - 1]
    
    lst_tmp = []
    for i in range(length):
        lst_tmp.append(nums[(length + i - k) % length])

    print(lst_tmp)

    for i in range(length):
        nums[i] = lst_tmp[i]

rotate(nums = [1,2,3,4,5,6,7], k = 3)
rotate(nums = [-1,-100,3,99], k = 2)
