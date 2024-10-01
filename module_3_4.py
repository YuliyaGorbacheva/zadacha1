def single_root_words(root_word, *other_word):
    same_words = []
    for word in other_word:
        if root_word in word in other_word:
            same_words.append(word)
        if root_word.lower() in other_word or word.lower() in root_word.lower():
            same_words.append(word)
    return same_words


print(single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies'))
print(single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel'))

single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
