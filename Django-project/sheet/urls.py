from django.urls import path
from .views import welcome_view 
from .import views

urlpatterns = [
    path('b/', views.welcome_view, name = 'home' )
]  