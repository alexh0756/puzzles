# def partition(s):

#     def is_palindrome(s):
#         i, j = 0, len(s) - 1

#         while i < j:
#             if s[i] != s[j]:
#                 return False
#             i += 1
#             j -= 1
#         return True
    
#     lst, splits = [], [0, len(s)]

#     while len(splits) < len(s) + 2:

#         i, lst_tmp = 0, []

#         while i < len(splits) - 1:
#             lst_tmp.append(s[splits[i]:splits[i+1]])
#             i += 1

#         lst_tmp_bool = list(map(is_palindrome, lst_tmp))
            
#         if len(lst_tmp_bool) == sum(lst_tmp_bool):
#             lst.append(lst_tmp)

#         if len(splits) > 2 and splits[1] < splits[2] - 1:
#             splits[1] += 1
#         else:
#             splits.insert(1, splits[0] + 1)

#     return lst


def partition(s):

    lst = [[val] for val in range(1, len(s)-1)]

    for lists in lst:
        lst1 = []
        for i in range(1, len(s)-1):
            if i in lists or i < lists[-1]:
                continue

            lst_tmp = [l for l in lists]
            lst_tmp.append(i)
            lst1.append(sorted(lst_tmp))
        lst.extend(lst1)
        if lst1 and len(lst1[0]) == len(s) - 2:
            break

    return lst

partition(s = "aabaac")
partition(s = "aab")
partition(s = "a")

