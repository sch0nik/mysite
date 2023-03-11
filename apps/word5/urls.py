from django.urls import path, include

from apps.word5.views import WordGame

urlpatterns = [
    path('', WordGame.as_view(), name='word_game'),
]
