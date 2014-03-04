from django.db import models

class Url(models.Model):
    url = models.CharField(max_length=100)
    ip = models.CharField(max_length=12)
