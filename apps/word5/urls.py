from django.urls import path, include

urlpatterns = [
    path('/', include('apps.word5.urls'), name='word_game'),
]
