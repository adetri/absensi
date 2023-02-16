from django.db import models
from anggota.models import Anggota


class Jam_absen(models.Model):
    start = models.TimeField(default="00:00:00")
    end = models.TimeField(default="00:00:00")
    deskripsi = models.CharField(max_length=100)

    def __str__(self):
        return "start : ({}) end: ({}) deskripsi: ({})".format(self.start, self.end, self.deskripsi)


class Absen(models.Model):

    jam_absen = models.TimeField(editable=False, auto_now_add=True)
    tgl_absen = models.DateField()
    anggota = models.ForeignKey(Anggota, on_delete=models.CASCADE, null=True)
    jam = models.ForeignKey(Jam_absen, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return "id : ({}) jam_absen: ({}) tgl_absem: ({}) anggota_id: ({}) ".format(self.id, self.anggota, self.jam_absen, self.tgl_absen)
