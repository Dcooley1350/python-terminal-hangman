# Returns array of indexes at which the character in question in the word

def check_word(character, word):
    indexes = []
    for n in range(len(word)):
        if character == word[n]:
            indexes.append(n)
    return indexes