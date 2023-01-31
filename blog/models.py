from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from ckeditor_uploader.fields import RichTextUploadingField


class Post(models.Model):
    title = models.CharField(max_length=125)
    url = models.SlugField()
    description = models.CharField(max_length=125)
    content = RichTextUploadingField()
    image = models.ImageField(blank=True)
    post_on = models.DateField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

