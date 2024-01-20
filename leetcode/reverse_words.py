def reverseWords(s):
    if len(s) == 0:
        return ""


    start_idx, end_idx = 0, 0
    string = ""
    for i in range(len(s)):
        if s[i] == ' ':
            if start_idx < end_idx:
                string = f"{s[start_idx:end_idx]} {string}"
            start_idx = i + 1
            end_idx = i + 1
            continue
        
        else:
            end_idx += 1

    if s[start_idx:end_idx] != (end_idx-start_idx)*' ':
        string = f"{s[start_idx:end_idx]} {string}"
    
    return string[:-1]

print(reverseWords('the sky is blue'))
print(reverseWords("  hello world  "))
print(reverseWords('a good  example'))