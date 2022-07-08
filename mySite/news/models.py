from django.db import models
from tinymce.models import HTMLField
from autoslug import AutoSlugField

# Create your models here.

class News(models.Model):
    title = models.CharField(max_length=100, default='')
    content = HTMLField()
    author = models.CharField(max_length=50)
    new_slug = AutoSlugField(populate_from='title', unique=True, null=True, default=None)
    news_image = models.FileField(upload_to='news/', max_length=255, null=True, default=None)