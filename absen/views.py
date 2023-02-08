from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic.base import TemplateView, View
from django.http import JsonResponse
from .form import *
from datetime import datetime
from django.views.decorators.csrf import csrf_exempt


class IndexView2(TemplateView):
    pass


# Create your views here.
def test(request):
    # posts = Post.objects.all()
    return render(request, 'index.html')


class ContextView(TemplateView):
    template_name = 'absen/test.html'

    def get_context_data(self):
        context = {
            'judul': 'TEST SCANER',
            'penulis': 'ujang',
        }

        return context


class absensi(View):
    template_name = 'absen/create_data.html'
    form = AbsensiForm()
    context = {}
    args = "teteteaaetststring"
    msg = ""

    def get(self, *args, **kwargs):
        if kwargs.__contains__('mg'):
            self.msg = kwargs['mg']

        self.context = {
            'judul': 'SCAN HERE',
            "akun_form": self.form,
            "msg": self.msg,
        }
        return render(self.request, self.template_name, self.context)

    def post(self, *args, **kwargs):

        jam = datetime.now().time().strftime("%H:%M")
        jam_mulai = datetime.strptime("06:00", "%H:%M").strftime("%H:%M")
        jam_terakhir = datetime.strptime("09:00", "%H:%M").strftime("%H:%M")
        # if jam >= jam_mulai and jam <=jam_terakhir:
        # 	pass
        # else:
        # 	msg="bukan Jam Untuk Absen"
        # 	return redirect('absen:status' , mg=(msg))

        self.form = AbsensiForm(self.request.POST)
        try:
            akun_info = Anggota.objects.get(slug=self.request.POST.get('slug'))

        except Anggota.DoesNotExist:
            msg = "Data Anggota Tidak Di temukan"
            return redirect('absen:status', mg=(msg))
        except Anggota.MultipleObjectsReturned:
            msg = "Multiple Absen Key"
            return redirect('absen:status', mg=(msg))

        data = akun_info.__dict__
        tgl = datetime.now().date().strftime("%Y-%m-%d")

        validasi_absen = Absen.objects.filter(
            anggota_id=data.get('id')).filter(tgl_absem=tgl)

        if len(validasi_absen) > 0:
            msg = "Anda Sudah Absen"
            return redirect('absen:status', mg=(msg))

        obj = Absen(anggota_id=data.get('id'), jam_absen=jam, tgl_absem=tgl)
        result = obj.save()

        if result is None:
            msg = "Absen Berhasil"
        else:
            msg = "save failed"

        return redirect('absen:status', mg=(msg))
