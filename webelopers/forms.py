from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm
from webelopers.models import *

from webelopers.models import Profile
DAYS_OF_WEEK = (
    (0, 'Saturday'),
    (1, 'Sunday'),
    (2, 'Monday'),
    (3, 'Tuesday'),
    (4, 'Wednesday'),
)


class SignUpForm(UserCreationForm):
	first_name = forms.CharField(max_length=30)
	last_name = forms.CharField(max_length=30)
	email = forms.EmailField(max_length=254)
	username = forms.CharField(max_length=100)
	password1 = forms.CharField(max_length=100)
	password2 = forms.CharField(max_length=100)

	class Meta:
		model = Account
		fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2',)

	def clean(self):
		cd = self.cleaned_data
		username = cd.get('username')
		if User.objects.filter(username=username).exists():
			self.add_error('username', "نام کاربری شما در سیستم موجود است")
		password1 = cd.get('password1')
		password2 = cd.get('password2')
		if password1 != password2:
			self.add_error('password2', "گذرواژه و تکرار گذرواژه یکسان نیستند")
		return cd


class ContactForm(forms.Form):
	title = forms.CharField(label='title', max_length=100)
	email = forms.EmailField(label='email', max_length=254)
	text = forms.CharField(label='text', min_length=10, max_length=250, widget=forms.Textarea)

	class Meta:
		fields = ('title', 'email', 'text',)


class LoginForm(forms.Form):
	username = forms.CharField(max_length=100)
	password = forms.CharField(max_length=100)

	class Meta:
		fields = ('username', 'password')


class searchform(forms.Form):
	search_query = forms.CharField(max_length=100)
	department = forms.BooleanField(initial=False, required=False)
	teacher = forms.BooleanField(initial=False, required=False)
	course = forms.BooleanField(initial=False, required=False)
	class Meta:
		fields = ('search_query', 'department', 'teacher', 'course')


class courseForm(ModelForm):
	class Meta:
		model = Course
		fields = ('department', 'name', 'course_number', 'group_number', 'teacher', 'start_time', 'end_time', 'first_day', 'second_day',)


class EditForm(ModelForm):
	first_name = forms.CharField(required=False)
	last_name = forms.CharField(required=False)
	document = forms.FileField(required=False)

	class Meta:
		model = Profile
		fields = ('first_name', 'last_name', 'document',)



