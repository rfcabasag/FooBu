from django.db import models
from django.contrib.auth.models import User

class RegisteredUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    is_owner = models.BooleanField(default=False)
    def __str__(self):
        return self.user.username

class Establishment(models.Model):
    owner = models.OneToOneField(RegisteredUser,on_delete=models.CASCADE)
    name = models.TextField(blank=True)
    desc = models.TextField(blank=True)
    area = models.TextField(blank=True)
    street = models.TextField(blank=True)
    def __str__(self):
        return self.name
