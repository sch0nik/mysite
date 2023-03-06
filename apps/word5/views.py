from django.shortcuts import render
from django.views.generic import TemplateView


class GameWord(TemplateView):
    template_name = 'game-word.html'
