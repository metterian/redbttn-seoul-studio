from django.db import models


class InstaData(models.Model):
    preview_photo = models.URLField()
    link = models.URLField()
    content = models.TextField()
