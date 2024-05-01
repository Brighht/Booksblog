from django.db import models
from datetime import datetime


# Create your models here.
class Posts(models.Model):
    objects = None
    title = models.CharField(max_length=100)
    date = models.DateTimeField(default=datetime.now,blank=True)
    content = models.CharField(max_length=10000000)
