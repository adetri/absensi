# Generated by Django 4.1.6 on 2023-02-08 14:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('anggota', '0001_initial'),
        ('absen', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='absen',
            name='anggota',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='anggota.anggota'),
            preserve_default=False,
        ),
    ]
