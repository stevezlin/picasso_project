from django import forms
from .models import UploadImage
from pyuploadcare.dj.forms import ImageField


class PostForm(forms.ModelForm):
    photo = ImageField(label='')

    class Meta:
        model = UploadImage
        fields = ('photo',)
