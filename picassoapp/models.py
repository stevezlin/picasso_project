from django.db import models
from pyuploadcare.dj.models import ImageField
from django.contrib.auth.models import User




# Model for uploadcare image upload


class UploadImage(models.Model):
    photo = ImageField(blank=True, manual_crop="")
    
    liked = models.ManyToManyField(
        User,
        related_name="liked_images",
    )
