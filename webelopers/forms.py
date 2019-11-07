from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
	first_name = forms.CharField(max_length=30)
	last_name = forms.CharField(max_length=30)
	email = forms.EmailField(max_length=254)
	username = forms.CharField(max_length=100)
	password1 = forms.CharField(max_length=100)
	password2 = forms.CharField(max_length=100)

	class Meta:
		model = User
		fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2',)


class ContactForm(forms.Form):
	title = forms.CharField(label='title', max_length=100)
	email = forms.EmailField(label='email', max_length=254)
	text = forms.CharField(label='text', min_length=10, max_length=250)

	class Meta:
		fields = ('title', 'email', 'text',)