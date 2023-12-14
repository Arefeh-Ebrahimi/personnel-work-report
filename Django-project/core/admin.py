from django.contrib import admin
from django.db import models
from django.shortcuts import reverse
from .models import Task

class TaskAdmin(admin.ModelAdmin):
    list_display = ('name','description','created_at', 'productivity', 'certainty', 'health_feeling', 'stage','project' )
    
admin.site.register(Task, TaskAdmin)

