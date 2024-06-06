from collections import Counter

def commonChar(words):

    counts = list(map(Counter, words))

    common = counts[0]
    i = 1
    while i < len(counts):
        cur_map = counts[i]
        j = 0
        chars = list(common.keys())
        while j < len(common):
            char = chars[j]
            if char not in cur_map:
                common.pop(char)
                chars.pop(j)
                continue
            if char in cur_map:
                common[char] = min(common[char], cur_map[char])
            j += 1
        i += 1

    return [char for char, num in common.items() for _ in range(num)]



commonChar(words = ["bella","label","roller"])
commonChar(words = ["cool","lock","cook"])
