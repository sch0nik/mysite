from util.finder import find_word, is_matches

with open('static/text/russian.txt', 'r') as f:
    list_word = f.readlines()
WORDS = [item[:-1] for item in list_word]


def test_existence():
    result = find_word('*****', ['а****'], '', WORDS)
    assert result
    result = find_word('**о**', ['а****'], '', WORDS)
    assert result


def test_letter_presence():
    result = find_word('*****', ['а****'], '', WORDS)
    for word in result:
        assert 'а' in word and word[0] != 'а'
    result = find_word('а****', ['*****'], '', WORDS)
    for word in result:
        assert word[0] == 'а'


def test_non_existence():
    result = find_word('*****', ['*****'], 'амт', WORDS)
    for word in result:
        assert 'а' not in word
        assert 'м' not in word
        assert 'т' not in word


def test_double_letters():
    result = find_word('*****', ['****а'], 'а', WORDS)
    for word in result:
        assert word.count('а') == 1, word

    result = find_word('а****', ['*****'], 'а', WORDS)
    for word in result:
        assert word.count('а') == 1, word

    result = find_word('****а', ['**а**'], 'а', WORDS)
    for word in result:
        assert word.count('а') == 1, word
