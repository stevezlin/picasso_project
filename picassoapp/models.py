from django.db import models
from pyuploadcare.dj.models import ImageField

# Post Model originally in Activity


class CreatePost(models.Model):
    username = models.CharField(max_length=30)
    text = models.TextField()

# Model for uploadcare image upload


class Post(models.Model):
    photo = ImageField(blank=True, manual_crop="")
