from django.db import models

class ebook(models.Model):
    title=models.TextField(null=True)
    author=models.TextField(null=True)
    genre=models.CharField(max_length=80)
    review=models.IntegerField(null=True)
    favourite = models.BooleanField(default=False)
