from django.contrib import admin
from django.db import models
from django.shortcuts import reverse
from .models import Post

class sheetAdmin(admin.ModelAdmin):
    list_display = ('name','text','datatime_created', 'Productivity', 'Certainty', 'Health_Feeling', 'Stage' )
    
admin.site.register(Post, sheetAdmin)

