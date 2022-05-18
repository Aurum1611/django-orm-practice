from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth


def signup(req):
    if req.method == 'POST':
        # Sign user up with provided information
        if req.POST['password'] == req.POST['pswd_confirm']:
            try:
                user = User.objects.get(username=req.POST['username'])
                # if no exception thrown, user already exists
                return render(req, 'accounts/signup.html', {'error': 'Username already taken'})
            except User.DoesNotExist:
                user = User.objects.create_user(req.POST['username'], password=req.POST['password'])
                auth.login(req, user)
                return redirect('homepage')
        else:
                return render(req, 'accounts/signup.html', {'error': 'Passwords must match'})
    else:
        # User wants to enter data to sign up
        return render(req, 'accounts/signup.html')


def login(req):
    if req.method == 'POST':
        # Login user with provided information
        user = auth.authenticate(username=req.POST['username'],password=req.POST['password'])
        if user:
            auth.login(req, user)
            return redirect('homepage')
        else:
            return render(req, 'accounts/login.html', {'error': 'username or password is incorrect'})
    else:
        # Display login page
        return render(req, 'accounts/login.html')


def logout(req):
    if req.method == 'POST':
        auth.logout(req)
        return redirect('homepage')
