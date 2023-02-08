# from django.conf.urls import url
from django.urls import path
from . import views
app_name = 'absen'
urlpatterns = [
    # path('', views.test),
    path('test', views.IndexView2.as_view(
        template_name='absen/test.html'), name="test"),
    path('new', views.ContextView.as_view()),
    # path('create', views.AnggotaFormView.as_view(), name='create_anggota'),
    path('', views.absensi.as_view(), name='absen'),
    path('status/<str:mg>/', views.absensi.as_view(), name='status'),


    # path('update/<str:update_id>', views.AnggotaFormView.as_view(mode='update'), name='update'),


]
