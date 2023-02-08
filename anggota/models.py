from django.db import models

# Create your models here.


class Anggota(models.Model):
    nama = models.CharField(max_length=100)
    slug = models.CharField(max_length=100)

    def __str__(self):
        return "id: ({}) nama:({}) slug:({}) ".format(self.id, self.nama, self.slug)
