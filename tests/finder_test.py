from util.finder import find_word, is_matches

with open('../static/text/russian.txt', 'r') as f:
    list_word = f.readlines()
LIST_WORD = [item[:-1] for item in list_word]


def find_word_test():
    situations = {
        'Ситуация 1': ('пол**', ['*****'], 'внаходис', ['полет', 'поляк', 'поляш']),
        'Ситуация 2': ('*а*ет', ['***та'], 'волнпсабг', ['жакет', 'замет', 'зачет', 'кадет', 'катет', 'макет', 'тацет']),
        'Ситуация 3': ('*о*ка', ['*****'], 'влндчкшгр', ['мойка', 'мотка', 'пойка', 'попка', 'сойка', 'сопка', 'соска', 'сотка', 'топка', 'тоска', 'фомка', 'фоска', 'сотка', 'топка', 'тоска', 'фомка', 'фоска']),
    }

    for situation in situations:
        template, list_templates, bad_letters, expected = situations[situation]
        received = find_word(template, list_templates, bad_letters, LIST_WORD)
        if received != expected:
            print(situation, '- bad')
        else:
            print(situation, '- ok')


find_word_test()
