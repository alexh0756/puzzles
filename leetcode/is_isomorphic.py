def is_isomorphic(s, t):

    str_map = {}

    for i in range(len(s)):
        if s[i] not in str_map and t[i] not in str_map.values():
            str_map[s[i]] = t[i]
        elif (s[i], t[i]) not in str_map.items():
            return False
        elif str_map[s[i]] == t[i]:
            continue
        else:
            return False

    return True

print(is_isomorphic(s = "badc", t = "baba"))
print(is_isomorphic(s = "egg", t = "add"))
print(is_isomorphic(s = "foo", t = "bar"))
print(is_isomorphic(s = "paper", t = "title"))