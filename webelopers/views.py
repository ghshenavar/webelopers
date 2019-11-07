from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.shortcuts import render
from webelopers.forms import *


def index(request):
	return render(request, 'homePage.html')


def registering(request):
	if request.method == 'POST':
		form = SignUpForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data.get('username')
			raw_password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=raw_password,)
			#login(request, user)
			return redirect('/')
	else:
		form = SignUpForm()

	return render(request, 'register.html', {'form': form})


def login(request):
	return render(request, 'login.html', {'form': form})


def contact(request):
	if request.method == 'POST':
		form = ContactForm(request.POST)
		if form.is_valid():
			return redirect('confirmation')
	else:
		form = forms.Form()
	return render(request, 'contact.html', {'form': form})


def confirmation(request):
	render(request, 'confirmed.html')