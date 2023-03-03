from django.db import models


class User(models.Model):
    name = models.CharField(max_length=200)
    title = models.CharField(max_length=200)