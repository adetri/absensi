
from django.contrib import admin
from django.urls import path, include

from .view import IndexView, ContextView, NewBase

urlpatterns = [
    path('admin/', admin.site.urls),
    path('absen/', include('absen.urls', namespace='absen')),
    path('anggota/', include('anggota.urls', namespace='anggota')),
    path('', IndexView.as_view(template_name='index.html')),
    path('contex', ContextView.as_view()),
    path('newbase', NewBase.as_view(template_name='newbase.html')),

]
