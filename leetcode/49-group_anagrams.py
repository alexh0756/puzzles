def groupAnagrams(strs):

    a_map = {}

    for string in strs:
        string_sorted = ''.join(sorted(string))
        if string_sorted not in a_map:
            a_map[string_sorted] = [string]
        elif string not in a_map[string_sorted]:
            a_map[string_sorted].append(string)
            

    return list(a_map.values())

print(groupAnagrams(strs = ["eat","tea","tan","ate","nat","bat"]))
print(groupAnagrams(strs = [""]))
print(groupAnagrams(strs = ["a"]))