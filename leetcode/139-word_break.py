def wordBreak(s, wordDict):

    progress = [0]
    wordDict = sorted(wordDict, reverse=True)

    while progress:
        tmp = []
        for prog in progress:
            for word in wordDict:
                if prog+len(word) in tmp:
                    continue

                if s[prog:prog+len(word)] == word:
                    tmp.append(prog+len(word))
        progress = tmp[:]
        if len(s) in progress:
            return True

    return False

print(wordBreak(s = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab", wordDict = ["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"]))
print(wordBreak(s = "leetcode", wordDict = ["leet","code"]))
print(wordBreak(s = "applepenapple", wordDict = ["apple","pen"]))
print(wordBreak(s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]))