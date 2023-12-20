# validation/forms.py
from django import forms

from .models import Participant,Vehicle

class RegisterForm(forms.ModelForm):
    class Meta:
        model = Participant
        fields = '__all__'

    def clean_firstname(self):
        first_name = self.cleaned_data['first_name']
        

class VehicleForm(forms.ModelForm):
    class Meta:
        model = Vehicle
        fields = '__all__'
    

