def scoreOfString(s):

    total = 0
    for i in range(len(s)-1):
        total += abs(ord(s[i]) - ord(s[i+1]))
    
    return total

scoreOfString(s = "hello")
scoreOfString(s = "zaz")