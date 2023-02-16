from django.db import models

# Create your models here.


class Anggota(models.Model):
    nama = models.CharField(max_length=100, default="")
    nama_orang_tua = models.CharField(max_length=100, default="")
    no_telp_orang_tua = models.CharField(max_length=100, default="")
    slug = models.CharField(max_length=100, default="")

    def __str__(self):
        return "id: ({}) nama:({}) slug:({}) ".format(self.id, self.nama, self.slug)
