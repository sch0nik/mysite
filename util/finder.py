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
    # слово должно соответствовать шаблону;
    # буквы из существующих должны быть в слове, но не на тех же местах;
    # в слове не должно быть букв из несуществующих, но могут быть одинаковые буквы в существующих и не существующих;
    result = []
    bad_letters = set(not_char)
    existing_letters = set(word) | set(''.join(list_chars))
    existing_letters.discard('*')
    common_letters = existing_letters & bad_letters

    for item in words:
        if len(item) != len(word):
            continue

        if (bad_letters - common_letters) & set(item):
            continue
        if common_letters:
            counter = [item for char in common_letters if item.count(char) >= 2]
            if counter:
                continue
        else:
            if bad_letters & set(item):
                continue

        # chars = bad_letters & set(item)
        # if bad_letters & set(word):
        #     counter = [item.count(i) for i in chars if item.count(i) > 1]
        #     if counter and chars:
        #         continue
        # elif bad_letters & set(''.join(list_chars)):
        #     counter = [item.count(i) for i in chars if item.count(i) > 1]
        #     if counter and chars:
        #         continue
        # elif chars:
        #     continue

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
