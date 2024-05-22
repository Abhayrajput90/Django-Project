from django.db import models

# Create your models here.
class SingUPform(models.Model):
    name = models.CharField(max_length=25)
    email = models.CharField(max_length=25)
    password = models.CharField(max_length=20)
    cpassword = models.CharField(max_length=20)
    option = models.CharField(max_length=20)