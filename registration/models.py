from django.db import models

# Create your models here.
class Users(models.Model):
    fullname = models.CharField(max_length=225)
    email = models.EmailField(max_length=225)
    password = models.CharField(max_length=225)
