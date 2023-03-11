from django import forms


class WordForm(forms.Form):
    template = forms.CharField(
        label='Слово',
        max_length=20,
        initial='*****',
        help_text='Шаблон слова, с желтыми буквами, без белых и серых',
        label_suffix=':',
    )
    valid_char = forms.CharField(
        label='Существующие буквы',
        max_length=50,
        initial='*****',
        help_text='Шаблон слова, с белыми буквами, без желтых и серых',
        label_suffix=':',
        required=True,
    )
    not_valid_char = forms.CharField(
        label='Только серые буквы',
        label_suffix=':',
        required=False,
    )
