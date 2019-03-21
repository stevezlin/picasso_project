from django.db import models
from pyuploadcare.dj.models import ImageField
from django.contrib.auth.models import User


# Post Model originally in Activity


class CreatePost(models.Model):
    username = models.CharField(max_length=50)
    text = models.TextField()
    liked = models.ManyToManyField(
        User,
        related_name="liked_posts",
    )
# Model for uploadcare image upload


class UploadImage(models.Model):
    photo = ImageField(blank=True, manual_crop="")
    
    liked = models.ManyToManyField(
        User,
        related_name="liked_images",
    )
