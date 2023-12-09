from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
# from django.forms import Form
from .forms import NewTimeForm
 
 
def welcome_view(request):
    
    if request.method == 'POST':
        form = NewTimeForm(request.POST)
        if form . is_valid():
            form.save()
            form = NewTimeForm()
        
    else:
        form = NewTimeForm()
        
    return render(request,'about.html', context={'form':form})
    
        