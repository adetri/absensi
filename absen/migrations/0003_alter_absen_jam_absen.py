# Generated by Django 4.1.6 on 2023-02-16 07:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('absen', '0002_rename_tgl_absem_absen_tgl_absen'),
    ]

    operations = [
        migrations.AlterField(
            model_name='absen',
            name='jam_absen',
            field=models.TimeField(auto_now_add=True),
        ),
    ]
