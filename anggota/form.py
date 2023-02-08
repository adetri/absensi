from django import forms
from .models import Anggota


class AnggotaForm(forms.ModelForm):
    class Meta:
        model = Anggota
        fields = [
            'nama',
            'slug',

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
        }
