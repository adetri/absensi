# Generated by Django 4.1.6 on 2023-02-16 05:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('anggota', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='anggota',
            name='nama_orang_tua',
            field=models.CharField(
                default='kosong', max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='anggota',
            name='no_orang_tua',
            field=models.CharField(
                default='kosong', max_length=100, null=True),
        ),
    ]
