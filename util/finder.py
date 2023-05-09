def is_matches(template, list_chars, word):
    for i, j in zip(template, word):
        if i == '*':
            continue
        if i != j:
            return False
    chars = []
    for item in list_chars:
        for i, j in enumerate(item):
            if j == '*':
                continue
            chars.append({'index': i, 'item': j})
    for i in chars:
        if i['item'] not in word or i['item'] == word[i['index']]:
            return False
    return True


def find_word(word, list_chars, not_char, words=None):
    if not words:
        return []
    result = []
    bad_letters = set(not_char)
    existing_letters = set(word) | set(''.join(list_chars))
    existing_letters.discard('*')
    common_bad_letters = existing_letters & bad_letters
    common_letters = bad_letters - common_bad_letters

    for item in words:
        if len(item) != len(word):
            continue

        if [i for i in common_bad_letters if item.count(i) > 1]:
            continue

        if common_letters & set(item):
            continue

        if not is_matches(word, list_chars, item):
            continue

        result.append(item)
    return result
