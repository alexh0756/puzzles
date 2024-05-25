def wordBreak(s, wordDict):

    lst = [[]]
    completed = []
    i = 0
    start = 0
    while i < len(lst):
        lst_tmp = lst[i]
        start = sum(list(map(len, lst_tmp)))
        for word in wordDict:

            if s[start:start+len(word)] == word:
                lst.append(lst_tmp + [word])
                if start+len(word) == len(s):
                    completed.append(' '.join(lst_tmp + [word]))

        i += 1
    return completed

print(wordBreak(s = "catsanddog", wordDict = ["cat","cats","and","sand","dog"]))
print(wordBreak(s = "pineapplepenapple", wordDict = ["apple","pen","applepen","pine","pineapple"]))
print(wordBreak(s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]))