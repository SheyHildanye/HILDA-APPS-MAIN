from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Post(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField(default='')  # Provide a default empty string
    date_posted = models.DateTimeField(default=timezone.now)  # Provide a default of timezone.now

    def __str__(self):
        return f'{self.title} | {self.author.username}'
