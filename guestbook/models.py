from django.db import models


class Blessing(models.Model):
    name = models.CharField(max_length=80)
    content = models.TextField()
    image = models.ImageField(upload_to='blessing')
