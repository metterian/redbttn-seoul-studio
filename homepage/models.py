from django.db import models


class InstaData(models.Model):
    preview_photo = models.URLField()
    # photo = models.ImageField()
    link = models.URLField()
    content = models.TextField()
