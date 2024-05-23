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
    
    def is_palindrome(s):
        i, j = 0, len(s) - 1

        while i < j:
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1
        return True

    splits = [[val] for val in range(1, len(s))]

    for prev_lst in splits:
        split_tmp = []
        for i in range(max(1, prev_lst[-1]+1), len(s)):
            if i in prev_lst or i < prev_lst[-1]:
                continue

            lst_tmp = [l for l in prev_lst]
            lst_tmp.append(i)
            split_tmp.append(sorted(lst_tmp))
        splits.extend(split_tmp)
        if split_tmp and len(split_tmp[0]) == len(s) - 1:
            break

    splits = [[]] + splits
    lst = []

    for split in splits:
        split = [0] + split + [len(s)]
        lst_tmp = []
        for i in range(len(split)-1):
            lst_tmp.append(s[split[i]:split[i+1]])
    
        lst_tmp_bool = list(map(is_palindrome, lst_tmp))
        if len(lst_tmp_bool) == sum(lst_tmp_bool):
            lst.append(lst_tmp)
    
    return lst

partition(s = "aabaac")
partition(s = "aab")
partition(s = "a")

