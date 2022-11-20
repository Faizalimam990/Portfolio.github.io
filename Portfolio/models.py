from django.db import models

class userprofiles(models.Model):
    email=models.CharField(max_length=12)
    text=models.CharField(max_length=100)