from django import forms
from .advertisment_models import Advertisement

class Insertadvertisment(forms.ModelForm):
    class Meta :
        model = Advertisement
        fields = ( 'pet', 'image1', 'image2')