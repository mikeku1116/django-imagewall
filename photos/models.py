from django.db import models
from django.utils import timezone


class Photo(models.Model):
    image = models.ImageField(upload_to='image/', blank=True, null=True)
    upload_date = models.DateField(default=timezone.now)

