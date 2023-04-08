import datetime
import json

from django.http import HttpResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt, requires_csrf_token
from django.views.generic import TemplateView

json_name = 'list_song.json'


class AvtoRadioInfo(TemplateView):
    template_name = 'avtoradio.html'

    def get_context_data(self, **kwargs):
        context = super(AvtoRadioInfo, self).get_context_data()
        try:
            list_song = json.load(open(json_name, 'r'))
        except FileNotFoundError:
            list_song = []
        context['list_song'] = list_song[::-1]
        return context


class DataAvtoradioView(TemplateView):
    def get(self, request, *args, **kwargs):
        summ = request.GET.get('summ')
        artist = request.GET.get('artist')
        title = request.GET.get('title')
        if not (summ and artist and title):
            return HttpResponse('')
        try:
            f = open(json_name, 'r')
            list_song = json.load(f)
        except FileNotFoundError:
            list_song = []
        list_song.append(
            {
                'data': str(datetime.datetime.now()),
                'summ': summ,
                'artist': artist,
                'title': title,
            }
        )
        with open(json_name, 'w') as f:
            json.dump(list_song[-20:], f, indent=4)

        return HttpResponse('')
