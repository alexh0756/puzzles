def isAnagram(s, t):

    if len(s) != len(t):
        return False

    map_counter = {}

    for char in s:
        if char not in map_counter:
            map_counter[char] = 1
        else:
            map_counter[char] += 1

    for char in t:
        if char not in map_counter:
            return False
        if map_counter[char] <= 0:
            return False
        else:
            map_counter[char] -= 1

    return True

print(isAnagram(s = "anagram", t = "nagaram"))
print(isAnagram(s = "rat", t = "car"))