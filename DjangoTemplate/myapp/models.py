from email import message
from pyexpat import model
from django.db import models
from django.contrib.auth.models import User


class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    message= models.TextField(max_length=500.)


    def __str__(self):
        return self.name
    


# Create your models here.
