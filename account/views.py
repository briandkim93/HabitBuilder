import re
from contextlib import suppress

from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib.auth.models import User

# Create your views here.
def signup(request):
    if request.method == 'POST':
        username = request.POST['username'].lower()
        password = request.POST['password']
        confirm_password = request.POST['confirm-password']
        email = request.POST['email']
        context = {
            'username': username,
            'password': password,
            'confirm_password': confirm_password,
            'email': email,
            'error': ''
        }
        if username and password and confirm_password and email:
            if len(username) < 5 or len(username) > 18:
                context['error'] = 'Username must be 5-18 characters long'
                return render(request, 'account/signup.html', context)
            if not re.match(r'^\w+$', username):
                context['error'] = 'Username may only contain letters, numbers, or underscores'
                return render(request, 'account/signup.html', context)   
            if len(password) < 5:
                context['error'] = 'Password must be 5 or more characters long'
                return render(request, 'account/signup.html', context)
            if password != confirm_password:
                context['error'] = 'Passwords did not match'
                return render(request, 'account/signup.html', context)   
            with suppress(User.DoesNotExist):
                email = User.objects.get(email=request.POST['email'])
                context['error'] = 'Email address is already taken'
                return render(request, 'account/signup.html', context)
            with suppress(User.DoesNotExist):
                user = User.objects.get(username=request.POST['username'])
                context['error'] = 'Username is already taken'
                return render(request, 'account/signup.html', context)
            user = User.objects.create_user(request.POST['username'], password=request.POST['password'], email=request.POST['email'])
            auth.login(request, user)
            return
        else:
            context['error'] = 'Please do not leave any empty fields'
            return render(request, 'account/signup.html', context)
    else:
        return render(request, 'account/signup.html')