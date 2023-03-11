from pprint import pprint


def is_matches(sample, list_chars, word):
    for i, j in zip(sample, word):
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
    for item in words:

        if len(item) != len(word):
            continue

        if set(not_char) & set(item):
            continue

        if not is_matches(word, list_chars, item):
            continue

        result.append(item)
    return result


if __name__ == '__main__':
    # шаблон слова
    word = '*****'
    # список букв не на местах
    words = [
        '*****',
    ]
    # несуществующие буквы
    not_char = 'вонпм'

    pprint(find_word(word, words, not_char, ['список слов']))
