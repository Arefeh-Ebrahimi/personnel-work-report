from django import forms
from .import models
from .models import Post 

class NewTimeForm(forms.ModelForm):
    class Meta : 
        model = Post
        
        fields = ['name','Productivity','Certainty','Health_Feeling','Stage','text']
