from django.db import models
from django.db.models.fields import DateTimeField

# Create your models here.

class Service(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=50)
    date = models.DateTimeField(auto_now_add=True)
    read_time = models.IntegerField()


class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=11, default=True, null=True)
    textarea = models.TextField()