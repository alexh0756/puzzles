def process_words(words, spaces, word_counter, maxWidth):

    if word_counter == 1:
        return words[1:],f"{words[0]}{' '*(maxWidth - len(words[0]))}"
    # elif word_counter == 2 and final:
    #     return words[2:], f"{words[0]} {words[1]}{' '*(maxWidth - len(words[0]) - len(words[1]))}"
    else:
        string = ''
        for i in range(word_counter):
            if i != word_counter-1:
                spaces_need = (word_counter-1-i)
                i_space = spaces // spaces_need
                i_space = i_space + 1 if i_space < spaces / spaces_need else i_space
                space_str = ' '*i_space
                spaces -= i_space
            else:
                space_str = ''

            string += f"{words[0]}{space_str}"
            words.pop(0)

    return words, string


def text_justification(words, maxWidth):

    array = []

    word_lens = [len(word) for word in words]

    length, word_counter = 0, 0
    for lens in word_lens:

        length += lens + 1

        if length - 1 > maxWidth:

            spaces = maxWidth - (length - 1 - lens - word_counter)
            words, string = process_words(words, spaces, word_counter, maxWidth)
            array.append(string)

            length, word_counter = lens + 1, 0

        word_counter += 1

    array.append(' '.join(words) + ' '*(maxWidth-length+1))

    return array

print(text_justification(words = ["The","important","thing","is","not","to","stop","questioning.","Curiosity","has","its","own","reason","for","existing."], maxWidth = 17))
print(["The     important","thing  is  not to","stop questioning.","Curiosity has its","own  reason   for","existing.        "])
print(text_justification(words = ["What","must","be","acknowledgment","shall","be"], maxWidth = 16))
print(text_justification(words = ["This", "is", "an", "example", "of", "text", "justification."], maxWidth = 16))