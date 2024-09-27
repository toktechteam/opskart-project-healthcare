from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('schedule/', views.book_appointment, name='schedule'),
]