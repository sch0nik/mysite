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
    template = '*****'
    list_template_exist = ['****а']
    bad_letter = 'а'

    received = find_word(template, list_template_exist, bad_letter, WORDS)
    expected = []
    for item in WORDS:
        if len(item) != len(template):
            continue
        if bad_letter not in item:
            continue
        if item[-1] == bad_letter:
            continue
        if item.count(bad_letter) > 1:
            continue
        expected.append(item)
    assert received == expected

    template = 'а****'
    list_template_exist = ['*****']
    received = find_word(template, list_template_exist, bad_letter, WORDS)
    expected = []
    for item in WORDS:
        if len(item) != len(template):
            continue
        if bad_letter not in item:
            continue
        if item[0] != bad_letter:
            continue
        if item.count(bad_letter) > 1:
            continue
        expected.append(item)
    assert received == expected

    list_template_exist = ['**а**']
    received = find_word(template, list_template_exist, bad_letter, WORDS)
    expected = []
    for item in WORDS:
        if len(item) != len(template):
            continue
        if bad_letter not in item:
            continue
        if item[2] == bad_letter or item[0] != bad_letter:
            continue
        if item.count(bad_letter) > 1:
            continue
        expected.append(item)
    assert received == expected
