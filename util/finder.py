from pprint import pprint


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
    result = []
    bad_letters = set(not_char)
    existing_letters = set(word) | set(''.join(list_chars))
    existing_letters.discard('*')
    common_letters = existing_letters & bad_letters

    for item in words:
        if len(item) != len(word):
            continue

        # trio = bad_letters & set(word) & set(''.join(list_chars))
        # if trio:
        #     counter = [let for let in trio if item.count(let) >= 3]

        if (bad_letters - common_letters) & set(item):
            continue
        # if common_letters:
        #     counter = [item for char in common_letters if item.count(char) >= 2]
        #     if counter:
        #         continue
        # else:
        #     if bad_letters & set(item):
        #         continue

        if not is_matches(word, list_chars, item):
            continue

        result.append(item)
    return result


if __name__ == '__main__':
    # шаблон слова
    sample = '*****'
    # список букв не на местах
    list_sample = [
        '*****',
    ]
    # несуществующие буквы
    not_chars = ''

    pprint(find_word(sample, list_sample, not_chars, ['список слов']))
