from django.urls import path

from apps.avtoradio_info.views import AvtoRadioInfo, DataAvtoradioView

urlpatterns = [
    path('', AvtoRadioInfo.as_view(), name='avtoradio'),
    path('data/', DataAvtoradioView.as_view()),
]
