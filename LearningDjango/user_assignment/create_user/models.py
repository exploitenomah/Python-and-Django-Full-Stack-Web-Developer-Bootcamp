from django.db import models

# Create your models here.

class MyUser(models.Model): 
  firstname = models.CharField(max_length=24)
  lastname = models.CharField(max_length=24)
  email = models.EmailField()