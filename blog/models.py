import datetime

from django.db import models
from django.db.models import *


class Post(models.Model):
    title = CharField(max_length=255)
    description = TextField()
    content = TextField()
    post_on = DateTimeField(auto_now=True)
    author = None

    def __str__(self):
        return self.title

