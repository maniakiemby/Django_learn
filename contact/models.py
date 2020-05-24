from django.db import models


class Contact(models.Model):
    title = models.CharField(max_length=120)