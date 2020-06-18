from django.db import models
from datetime import date


# Create your models here.

class timetable(models.Model):
    title = models.CharField(max_length=50)
    discription = models.TextField()
    deadline = models.DateField(default=date.today)
    status = models.BooleanField(default=False)
