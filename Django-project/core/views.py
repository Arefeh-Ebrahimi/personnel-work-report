from django.shortcuts import render
from django.http import HttpResponse
from .models import Task
from .forms import TaskForm
 
 
def welcome_view(request):
    
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form . is_valid():
            form.save()
            form = TaskForm()
        
    else:
        form = TaskForm()
        
    return render(request,'about.html', context={'form':form})
