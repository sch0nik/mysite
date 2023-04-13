from util.finder import find_word, is_matches

with open('../static/text/russian.txt', 'r') as f:
    list_word = f.readlines()
LIST_WORD = [item[:-1] for item in list_word]


def find_word_test():
    situations = {
        'Ситуация 1': ('пол**', ['*****'], 'внаходис', ['полёт', 'поляк', 'поляш']),
        'Ситуация 2': ('пол**', ['*****'], 'внаходис', ['полёт', 'поляк', 'поляш']),
    }

    for situation in situations:
        template, list_templates, bad_letters, expected = situations[situation]
        received = find_word(template, list_templates, bad_letters, LIST_WORD)
        if received != expected:
            print(situation, '- bad')
        else:
            print(situation, '- ok')


find_word_test()
