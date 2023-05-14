def is_matches(word, template, chars):
    for ind, ch in enumerate(word):
        if template[ind] != '*' and ch != template[ind]:
            return False
        if ch in chars[ind]:
            return False
    return True


def find_word(template, list_chars, not_char, words=None):
    if not words:
        return []
    length = len(template)
    set_template = set(template)
    list_chars = list(map(lambda x: x.ljust(length, '*') if len(x) < length else x[:5], list_chars))
    bad_chars = set(not_char)
    existing_chars = set(''.join(list_chars))
    common_chars = bad_chars & existing_chars & set_template
    existing_chars = existing_chars | set_template
    existing_chars.discard('*')
    common_existing_chars = bad_chars & existing_chars or bad_chars & set_template
    bad_chars = bad_chars - existing_chars

    chars = [(), (), (), (), ()]
    for i in list_chars:
        for ind, j in enumerate(i):
            chars[ind] += (j,)

    result = []
    for word in words:
        set_word = set(word)
        if len(word) != length:
            continue
        if not existing_chars & set_word:
            continue
        if set_word & bad_chars:
            continue
        if common_chars and is_matches(word, template, chars):
            result.append(word)
            continue
        if common_existing_chars:
            if [i for i in common_existing_chars if word.count(i) > 1]:
                continue
        if not is_matches(word, template, chars):
            continue
        result.append(word)
    return result

# with open('../static/text/russian.txt', 'r') as f:
#     list_word = f.readlines()
# WORDS = [item[:-1] for item in list_word]
#
# print(find_word('а****', ['*****'], 'а', WORDS))
