from django.urls import path
from . import views

urlpatterns = [
    path('profile/', views.profile, name='profile'),
    path('appointments/', views.manage_schedule, name='appointments'),
]