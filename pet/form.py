from django import forms
from .models import Pet


class InsertPet(forms.ModelForm):
    class Meta:
        model = Pet
        fields = ('age','type', 'color', 'gender','breed','weight','image')