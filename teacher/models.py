from django.db import models

class Teacher(models.Model):
     nuptk = models.CharField(max_length=20, unique=True)
     name = models.CharField(max_length=100)
     gender = models.BooleanField(default=True)

     def __str__(self):
          return self.name