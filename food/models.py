from django.db import models
from django.contrib.auth.models import User

class RegisteredUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    is_owner = models.BooleanField(default=False)
    def __str__(self):
        return self.user.username

class Establishment(models.Model):
    id = models.AutoField(primary_key=True)
    owner = models.ForeignKey(RegisteredUser,blank=False,on_delete=models.CASCADE)
    name = models.TextField(blank=True)
    desc = models.TextField(blank=True)
    area = models.TextField(blank=True)
    street = models.TextField(blank=True)
    def __str__(self):
        return self.name

class FoodItem(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.TextField(blank=True)
    price = models.DecimalField(decimal_places=2,max_digits=10)
    est = models.ForeignKey(Establishment, blank=False, null=False, on_delete=models.CASCADE)
    def __str__(self):
        return self.name

class Rates(models.Model):
    rating = models.DecimalField(decimal_places=2,max_digits=3)
    cus = models.ForeignKey(RegisteredUser,blank=False,on_delete=models.CASCADE)
    est = models.ForeignKey(Establishment,blank=False,on_delete=models.CASCADE)

class Favorites(models.Model):
    cus = models.ForeignKey(RegisteredUser,blank=False,on_delete=models.CASCADE)
    est = models.ForeignKey(Establishment,blank=False,on_delete=models.CASCADE)