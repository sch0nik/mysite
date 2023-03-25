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
    bad_char = set(not_char)
    for item in words:
        if len(item) != len(word):
            continue

        chars = bad_char & set(item)
        if bad_char & set(word):
            counter = [item.count(i) for i in chars if item.count(i) > 1]
            if counter and chars:
                continue
        elif bad_char & set(''.join(list_chars)):
            counter = [item.count(i) for i in chars if item.count(i) > 1]
            if counter and chars:
                continue
        elif chars:
            continue

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
    not_chars = 'вонпм'

    pprint(find_word(sample, list_sample, not_chars, ['список слов']))
