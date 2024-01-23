from django.db import models

# Create your models here.
class Home(models.Model):
    email = models.CharField(max_Length = 120)
    name = models.CharField(max_Length = 120)
    password = models.CharField(max_Length = 20)
    