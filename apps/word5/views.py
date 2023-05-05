from django.views.generic import TemplateView

from util.finder import find_word
from .forms import WordForm

with open('static/text/russian.txt', 'r') as f:
    list_word = f.readlines()
LIST_WORD = sorted([item[:-1] for item in list_word])


class WordGame(TemplateView):
    template_name = 'word-game.html'
    form = WordForm

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)

        template_word = request.GET.get('template')
        valid_char = request.GET.get('valid_char')
        not_valid_char = request.GET.get('not_valid_char')

        template_word = template_word.strip().lower() if template_word else '*****'
        valid_char = valid_char if valid_char else '*****'
        valid_char = valid_char.split(',')
        valid_char = list(map(lambda x: x.strip().lower(), valid_char))
        not_valid_char = not_valid_char.strip().lower() if not_valid_char else ''

        context['form'] = self.form(
            initial={
                'template': template_word,
                'valid_char': ', '.join(valid_char),
                'not_valid_char': not_valid_char,
            }
        )
        context['list_word'] = find_word(template_word, valid_char, not_valid_char, LIST_WORD)

        return self.render_to_response(context)
