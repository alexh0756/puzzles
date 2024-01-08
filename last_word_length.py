def last_word_length(s):

    if len(s) == 0:
        return 0

    n_chars = len(s)

    while n_chars > 0:
            if ' ' != s[n_chars-1]:
                break
            n_chars -= 1

    length = 0
    for i in range(n_chars, -1, -1):
        if ' ' == s[i-1]:
            return length
        length += 1

    return length

print(last_word_length('some important thing'))
print(last_word_length("Hello World"))
print(last_word_length("   fly me   to   the moon  "))
print(last_word_length("luffy is still joyboy"))