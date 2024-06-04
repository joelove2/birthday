from django import forms
from .models import Participant

    

class ParticipantForm(forms.ModelForm):
    class Meta:
        model = Participant
        fields = ['name', 'phone_number', 'email', 'registration_type']
       
    widgets = {
            'registration_type': forms.Select(choices=Participant.REGISTRATION_TYPES),
        }
    