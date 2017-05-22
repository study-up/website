from django.db import models


class Mood(models.Model):
    text = models.TextField()
    picture = models.ImageField()
    created = models.DateTimeField(auto_now_add=True)
