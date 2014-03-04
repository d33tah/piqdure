from django.db import models

class Url(models.Model):
    number = models.AutoField(primary_key=True)
    url = models.CharField(max_length=100)
    ip = models.CharField(max_length=12)
