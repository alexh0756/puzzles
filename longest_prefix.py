def longestCommonPrefix(strs):

    if len(strs) <= 1:
        return ""
    if len(strs) == 1:
        return strs[0]
    if "" in strs:
        return ""

    prefix = ""
    cont_loop = True
    
    counter = 0
    while cont_loop:
        for i in range(1, len(strs)):
            if counter in (len(strs[0]), len(strs[i])):
                cont_loop = False
                break

            elif strs[0][counter] != strs[i][counter]:
                cont_loop = False
                break

        counter += 1

    return strs[0][:counter-1]

print(longestCommonPrefix(strs = [""]))
print(longestCommonPrefix(strs = ["a", "ac"]))
print(longestCommonPrefix(strs = ["ab", "a"]))
print(longestCommonPrefix(strs = ["flight", "flow", "flower"]))
print(longestCommonPrefix(strs = ["dog","racecar","car"]))
