def replaceWords(dictionary, sentence):

    lengths = []
    for word in dictionary:
        if len(word) not in lengths:
            lengths.append(len(word))

    dictionary = set(dictionary)
    new = []
    sentence = sentence.split(' ')
    for word in sentence:
        appended = False
        i = 0
        while i < len(lengths) and not appended:
            length = lengths[i]
            if len(word) >= length and word[:length] in dictionary:
                new.append(word[:length])
                appended = True
                break
            i += 1
        if not appended:
            new.append(word)

    return ' '.join(new)


print(replaceWords(
    dictionary = ["catt","bat","rat"], 
    sentence = "the cattle was rattled by the battery"
    )
)

print(replaceWords(
    dictionary = ["a","b","c"], 
    sentence = "aadsfasf absbs bbab cadsfafs"
    )
)