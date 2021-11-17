from django.db import models
from random import randrange
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,related_name="profile")
    CHILD = "C"
    PARENT = "P"
    ROLE_CHOICES = [
        (CHILD, 'Child'),
        (PARENT, 'Parent'),
    ]  
    firstname = models.TextField(max_length=100)
    lastname = models.TextField(max_length=100) 
    family_code = models.PositiveIntegerField(default=randrange(1000000, 2000000))
    role = models.CharField(
        max_length=1,
        choices=ROLE_CHOICES,
        default=PARENT,
        ) 
    
    def __str__(self) -> str:
        return self.firstname
