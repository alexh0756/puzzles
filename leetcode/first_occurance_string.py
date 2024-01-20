def strStr(haystack, needle):

    stack = ''

    for i, char in enumerate(haystack):

        stack += char

        if stack in needle:
            if len(stack) == len(needle):
                return i - len(stack) + 1
            
        else: 
            stack = stack[1:]

    return -1
    

print(strStr(haystack = "mississippi", needle = "issip"))
print(strStr(haystack = "sadbutsad", needle = "sad"))
print(strStr(haystack = "leetcode", needle = "leeto"))