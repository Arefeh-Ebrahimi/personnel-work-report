from django import forms
from .import models
from .models import Task 

class TaskForm(forms.ModelForm):
    class Meta : 
        model = Task
        
        fields = ['name','productivity','certainty','health_feeling','stage','project', 'description']
