from django import forms
from django.forms import ModelForm

from .models import *


class TaskForm(forms.ModelForm):
	class Meta:
		model = Task
		fields = ['title', 'description', 'picture']

class UpdateForm(forms.ModelForm):
	class Meta:
		model = Task
		fields = '__all__'
