from django.db import models

# Create your models here.
class Teacher(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    city = models.CharField(max_length=50)