from django.shortcuts import render
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic.base import TemplateView, View
from django.http import JsonResponse
from .form import *
from datetime import datetime
from django.views.decorators.csrf import csrf_exempt
from absen.models import Absen
# Create your views here.


class Data_anggota(TemplateView):

    def get_context_data(self):
        semua_anggota = Anggota.objects.all()
        context = {
            'page_title': 'Data Anggota',
            'semua_anggota': semua_anggota,
        }
        return context


class AnggotaFormView(View):
    template_name = 'anggota/form_anggota.html'
    form = AnggotaForm()
    mode = None
    context = {}

    def get(self, *args, **kwargs):
        if self.mode == 'update':
            akun_update = Anggota.objects.get(id=kwargs['update_id'])
            data = akun_update.__dict__
            self.form = AnggotaForm(initial=data, instance=akun_update)

        elif self.mode == 'delete':
            Anggota.objects.filter(id=kwargs['delete_id']).delete()
            return redirect('anggota:data_anggota')

        self.context = {
            "judul": "Tambah akun",
            "akun_form": self.form,
        }

        return render(self.request, self.template_name, self.context)

    def post(self, *args, **kwargs):
        print(kwargs)
        if kwargs.__contains__('delete_id'):
            pass
        else:

            if kwargs.__contains__('update_id'):
                # pass
                akun_update = Anggota.objects.get(id=kwargs['update_id'])
                self.form = AnggotaForm(
                    self.request.POST, instance=akun_update)
            else:
                self.form = AnggotaForm(self.request.POST)

            if self.form.is_valid():
                self.form.save()

        return redirect('anggota:data_anggota')


class Data_absen(TemplateView):

    def get_context_data(self):
        anggota = Absen.objects.select_related('anggota').all()

        context = {
            'judul': 'Data Absen',
            'anggota': anggota,
        }

        return context
