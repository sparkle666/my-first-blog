from django import forms
from .models import Post

class PostForm(forms.ModelForm):
	class Meta:
		model = Post
		fields = ("title", "body")

class ContactForm(forms.Form):
	first_name = forms.CharField(max_length=100, label='First Name', widget = forms.TextInput(attrs={'class': 
		'w3-input'}))
	last_name = forms.CharField(label='Last Name', widget = forms.TextInput(attrs={'class': 
		'w3-input'}))

class Add(forms.Form):
	num1 = forms.IntegerField()
	num2 = forms.IntegerField()
	

