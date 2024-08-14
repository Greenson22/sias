from django.db import models

# Create your models here.
class Teacher(models.Model):
     nuptk = models.CharField(max_length=20, unique=True)
     nama = models.CharField(max_length=100)
     gender = models.BooleanField(default=True)

     def __str__(self):
          pass