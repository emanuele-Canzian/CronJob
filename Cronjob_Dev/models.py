from django.contrib.auth.models import User
from django.db import models


class CronJob(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)

    title = models.CharField(max_length=128, null=False, default='')

    url = models.URLField(max_length=255, null=False, default='')

    auth = models.BooleanField(default=False)

    username = models.CharField(max_length=30, null=True, default='')

    password = models.CharField(max_length=30, null=True, default='')

    minute = models.CharField(max_length=30, null=False, default='')

    hour = models.CharField(max_length=30, null=False, default='')

    dayOfMonth = models.CharField(max_length=30, null=False, default='')

    month = models.CharField(max_length=30, null=False, default='')

    weekday = models.CharField(max_length=30, null=False, default='')

    cronejob = models.CharField(max_length=30, null=True)

    class meta:
        ordering = ['-id']


    def __str__(self):
        return f"{self.title} - {self.url}"
