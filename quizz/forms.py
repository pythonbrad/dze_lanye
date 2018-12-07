from django import forms
from django.contrib.auth.models import User
from .models import Remark
from django.utils import timezone

class SigninForm(forms.ModelForm):
	class Meta:
		model = User
		fields = ['username','first_name','last_name','email','password']
		widgets = {
			'password':forms.PasswordInput(),
		}
	def clean_username(self):
		data = self.cleaned_data['username']
		if len(data) <= 4:
			raise forms.ValidationError("Ton nom d'utilisateur doit avoir plus de 4 caracteres")
		return data
	def clean_password(self):
		data = self.cleaned_data['password']
		if len(data) <= 4:
			raise forms.ValidationError("Tom mot de passe doit avoir plus de 4 caracteres")
		return data

class LoginForm(forms.Form):
	username_or_email = forms.CharField()
	password = forms.CharField(widget=forms.PasswordInput())

class RemarkForm(forms.ModelForm):
	class Meta:
		model = Remark
		fields = ['remark_text']