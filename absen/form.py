from django import forms
from .models import *
from anggota.models import Anggota

# class AnggotaForm(forms.ModelForm):
# 	class Meta:
# 		model = Anggota
# 		fields = [
# 			'nama',
# 			'slug',

# 		]


class AbsensiForm(forms.ModelForm):
    slug = forms.CharField()

    class Meta:
        model = Anggota
        fields = [
            'slug',
        ]
