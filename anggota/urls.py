# from django.conf.urls import url
from django.urls import path
from . import views
app_name = 'anggota'
urlpatterns = [
    path('', views.Data_anggota.as_view(
        template_name='anggota/data_anggota.html'), name='data_anggota'),
    path('create', views.AnggotaFormView.as_view(), name='create_anggota'),
    path('update/<str:update_id>',
         views.AnggotaFormView.as_view(mode='update'), name='update_anggota'),
    path('delete/<str:delete_id>',
         views.AnggotaFormView.as_view(mode='delete'), name='delete_anggota'),
    path('absensi', views.Data_absen.as_view(
        template_name='anggota/data_absen.html'), name='data_absen'),
]
