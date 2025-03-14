from django.db import models
from django.contrib.auth.models import User
from localflavor.py_ import py_department
from .utils import user_directory_path

class Location(models.Model):
    address_1= models.CharField(max_length= 128)
    address_2= models.CharField(max_length= 128, blank=True)
    city= models.CharField(max_length=64)
    department= models.CharField(max_length=2, choices=py_department.DEPARTMENT_CHOICES, default='AS')
    
    def __str__(self):
        return f'Location {self.id}'

class Profile (models.Model):
    user= models.OneToOneField(User, on_delete=models.CASCADE)
    photo= models.ImageField(upload_to= user_directory_path,null=True)
    bio= models.CharField(max_length=140, blank=True)
    phone_number= models.CharField(max_length=15, blank=True)
    location= models.OneToOneField(Location, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f'{self.user.username}\'s Profile'
