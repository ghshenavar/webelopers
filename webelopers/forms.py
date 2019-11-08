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


# def clean(self):
# 	cd = self.cleaned_data
# 	username = cd.get('username')
# 	user = User.objects.filter(username=username)
# 	if user is not None:
# 		raise forms.ValidationError("نام کاربری شما در سیستم موجود است")
# 	if "password1" in cd and "password2" in cd:
# 		if cd["password1"] != cd["password2"]:
# 			self._errors["password2"] = self.error_class(['گذرواژه و تکرار گذرواژه یکسان نیستند'])
# 			del cd['password2']
# 	return cd


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


class EditForm(forms.Form):
	first_name = forms.CharField(max_length=100, required=False)
	last_name = forms.CharField(max_length=100, required=False)

	class Mate:
		fields = ('first_name', 'last_name')
