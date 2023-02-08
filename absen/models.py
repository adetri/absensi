from django.db import models
from anggota.models import Anggota


class Absen(models.Model):

    jam_absen = models.TimeField(editable=False)
    tgl_absem = models.DateField()
    anggota = models.ForeignKey(Anggota, on_delete=models.CASCADE)

    def __str__(self):
        return "id : ({}) jam_absen: ({}) tgl_absem: ({}) anggota_id: ({}) ".format(self.id, self.anggota, self.jam_absen, self.tgl_absem)
