from django.db import models

# Create your models here.

class Project(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='images/')
    summary = models.CharField(max_length=200)
    ur = models.CharField(max_length=100)

    def __str__(self):
        return self.title
    