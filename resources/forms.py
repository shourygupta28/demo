from django import forms
from .models import *

class ResourceForm(forms.ModelForm):
	
	class Meta(UserCreationForm.Meta):
		model 		= User
		fields 		= ['title','description','file','password2']
