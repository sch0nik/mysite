from django.urls import path, include

from mysite.views import IndexPage

urlpatterns = [
    path('', IndexPage.as_view(), name='index'),
    path('word-game/', include('apps.word5.urls')),
    path('avtoradio-info/', include('apps.avtoradio_info.urls')),
    # path('admin/', admin.site.urls),
]
