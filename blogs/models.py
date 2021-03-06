from django.db import models

# Create your models here.

class Blog(models.Model):
    title = models.CharField(max_length=200)
    pubdate = models.DateTimeField()
    image = models.ImageField(upload_to='images/')
    summary = models.TextField()