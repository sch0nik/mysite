from django.urls import path, include

from apps.word5.views import GameWord

urlpatterns = [
    path('', GameWord.as_view(), name='game_word'),
]
