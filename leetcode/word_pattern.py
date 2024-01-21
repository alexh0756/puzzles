def word_pattern(pattern, s):

    lst = s.split(' ')
    word_map = {}
    
    if len(pattern) != len(lst):
        return False

    for i, word in enumerate(lst):
        if pattern[i] not in word_map and word not in word_map.values():
            word_map[pattern[i]] = word
        elif (pattern[i], word) not in word_map.items():
            return False
        elif word_map[pattern[i]] == word:
            continue 
        else:
            return False 

    return True

print(word_pattern(pattern = "abba", s = "dog cat cat dog"))
print(word_pattern(pattern = "abba", s = "dog dog dog dog"))
print(word_pattern(pattern = "abba", s = "dog cat cat fish"))
print(word_pattern(pattern = "aaaa", s = "dog cat cat dog"))