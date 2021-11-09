from django import forms
from .models import Doctor_form


class Insert_appoinment(forms.ModelForm):
    class Meta:
        model = Doctor_form
        fields = ('Patient_type','Patient_owner_name', 'patient_owner_phone_no', 'pet_age','pet_gender',
                  'pet_problem','date_time')

