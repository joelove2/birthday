from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ParticipantForm
#from .models import Participant


def home(request):
     return render(request, 'home.html', {})
    
def register(request):
    if request.method == 'POST':
        form = ParticipantForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "You Have Registered Successfully!")
            return redirect('home')
    else:
        form = ParticipantForm()
    return render(request, 'register.html', {'form': form})

