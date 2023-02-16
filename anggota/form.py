from django import forms
from .models import Anggota


class AnggotaForm(forms.ModelForm):
    class Meta:
        model = Anggota
        fields = [
            'nama',
            'slug',
            'nama_orang_tua',
            'no_telp_orang_tua',


        ]

        widgets = {
            'nama': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Isi dengan Nama'
                }),
            'slug': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'slug target'
                }),
            'nama_orang_tua': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'slug target'
                }),
            'no_telp_orang_tua': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'slug target'
                }),
        }
