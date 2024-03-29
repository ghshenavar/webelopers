from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.shortcuts import render, redirect
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
			return redirect('/')
	else:
		form = SignUpForm()

	return render(request, 'register.html', {'form': form})


def Login(request):
	error = False
	if request.method == 'POST':
		form = LoginForm(request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				return redirect('/')
			error = True
	else:
		form = LoginForm()
	return render(request, 'login.html', {'form': form, 'error': error})


def contact(request):
	if request.method == 'POST':
		form = ContactForm(request.POST)
		if form.is_valid():
			subject = form.cleaned_data.get('title')
			email = form.cleaned_data.get('email')
			text = form.cleaned_data.get('text')
			x = ''
			y = x + email + '\n' + text
			send_mail(subject, y, 'dornaaadehghani@gmail.com', ['‫‪webe19lopers@gmail.com', 'dornadehghani@ymail.com'])
			return redirect('confirmed/')
	else:
		form = ContactForm()
	return render(request, 'contact.html', {'form': form})


def confirmation(request):
	return render(request, 'confirmation.html')


def logout_view(request):
	logout(request)
	return redirect('/')


@login_required
def profile(request):
	first_name = request.user.first_name
	last_name = request.user.last_name
	username = request.user.username
	context = {'first_name': first_name,
			   'last_name': last_name,
			   'username': username,
			   }
	return render(request, 'profile.html', context)


@login_required
def panel(request):
	return render(request, 'panel.html')


def add_course(request):
	if request.method == 'POST':
		form = courseForm(request.POST)
		if form.is_valid():
			data = form.cleaned_data
			c = Course(department=data['department'], name=data['name'], course_number=data['course_number'],
					   group_number=data['group_number'], teacher=data['teacher'], start_time=data['start_time'],
					   end_time=data['end_time'], first_day=data['first_day'], second_day=data['second_day'],)
			c.second_day = 10
			c.save()
			return redirect('/')
	else:
		form = courseForm()
	return render(request, 'course.html', {'form': form})


def courses(request):
	search = False
	if request.method == 'POST':
		form = searchform(request.POST)
		if form.is_valid():
			search_query = form.cleaned_data.get('search_query')
			if form.cleaned_data.get('course'):
				courses = Course.objects.filter(name=search_query)
			elif form.cleaned_data.get('teacher'):
				courses = Course.objects.filter(teacher=search_query)
			else:
				courses = Course.objects.filter(department=search_query)
			search = True
		form = searchform()
	else:
		form = searchform()
		courses = Course.objects.all()
	return render(request, 'courses.html', {'courses': courses, 'form': form, 'search': search})


@login_required
def edit(request):
	form = EditForm(request.POST or None, request.FILES)
	if request.method == 'POST':
		if form.is_valid():
			fname = form.cleaned_data.get('first_name')
			lname = form.cleaned_data.get('last_name')
			img = form.cleaned_data.get('document')
			if fname:
				request.user.first_name = fname
				request.user.save()
			if lname:
				request.user.last_name = lname
				request.user.save()
			if img:
				request.user.image = img
				request.user.save()
			return redirect('/profile')
		else:
			form = EditForm()
	return render(request, 'edit.html', {'form': form})
