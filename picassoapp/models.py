from django.db import models

# Create your models here.

class CreatePost(models.Model):
    username = models.CharField(max_length=30)
    text = models.TextField()
