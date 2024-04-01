from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.conf import settings
from django.core.mail import send_mail
from django.contrib import messages
from .forms import SignUp

def signup(request):
    form = SignUp()
    if request.method == 'POST':
        form = SignUp(request.POST)
        if form.is_valid():
            subject = 'Welcome to Arshaq Media'
            message = f"Hi,{form.cleaned_data.get('username')}  This is a success message from ArshaqMedia through Django"
            email_from = settings.EMAIL_HOST_USER
            recipient_list = form.cleaned_data.get('email')
            
            send_mail(subject, message, email_from, [recipient_list])
            messages.success(request, 'Email sent successfully..')
            return redirect('home')
    return render(request, 'home.html', {'form':form})