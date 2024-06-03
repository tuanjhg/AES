from django import forms
from .models import Stuff

class StuffForm(forms.ModelForm):
    class Meta:
        model = Stuff
        fields = ['profile_image', 'firstname', 'lastname', 'dob', 'phone', 'address']
        widgets = {
            'dob': forms.DateInput(attrs={'type': 'date'}),
        }