from django.db import models
from django.contrib.auth.models import User

class Provider(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    specialty = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    address = models.TextField()

    def __str__(self):
        return f'Dr. {self.user.last_name}' if self.user.last_name else self.user.username

class Schedule(models.Model):
    provider = models.ForeignKey(Provider, on_delete=models.CASCADE)
    available_from = models.DateTimeField()
    available_to = models.DateTimeField()