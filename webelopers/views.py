from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from pathlib import Path
import smtplib

from django.core.mail import send_mail
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
			user = authenticate(username=username, password=raw_password)
			# login(request, user)
			return redirect('/')
	else:
		form = SignUpForm()

	return render(request, 'register.html', {'form': form})


def login(request):
	if request.method == 'POST':
		form = LoginForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			return redirect('confirmed/')
	else:
		form = LoginForm()
	return render(request, 'login.html', {'form': form})


def contact(request):
	if request.method == 'POST':
		form = ContactForm(request.POST)
		if form.is_valid():
			subject = form.cleaned_data.get('title')
			email = form.cleaned_data.get('email')
			text = form.cleaned_data.get('text')
			x=''
			y=x+email+'\n'+text
			send_mail(subject, y, 'dornaaadehghani@gmail.com', ['‫‪webe19lopers@gmail.com', ])
			return redirect('confirmed/')
	else:
		form = ContactForm()
	return render(request, 'contact.html', {'form': form})


def confirmation(request):
	return render(request, 'confirmation.html')
