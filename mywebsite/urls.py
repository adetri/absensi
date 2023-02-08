
from django.contrib import admin
from django.urls import path, include

from .view import IndexView, ContextView, NewBase
from anggota.views import *
urlpatterns = [
    path('admin/', admin.site.urls),
    path('absen/', include('absen.urls', namespace='absen')),
    path('anggota/', include('anggota.urls', namespace='anggota')),
    path('',  Data_anggota.as_view(
        template_name='anggota/data_anggota.html')),

    path('contex', ContextView.as_view()),
    path('newbase', NewBase.as_view(template_name='newbase.html')),

]
