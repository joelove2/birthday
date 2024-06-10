from django import forms
from .models import Participant

    

class ParticipantForm(forms.ModelForm):
    class Meta:
        model = Participant
        fields = ['name', 'phone_number', 'email', 'registration_type']
       
    widgets = {
        'name': forms.TextInput(attrs={'class':'form-control'}),
        'phone_number': forms.NumberInput(attrs={'class':'form-control'}),
        'email': forms.EmailInput(attrs={'class':'form-control'}),

        'registration_type': forms.Select(choices=Participant.REGISTRATION_TYPES),
        }
    