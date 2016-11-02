from __future__ import unicode_literals

from django.db import models


class FourVideoStream(models.Model):

    title = models.CharField(max_length=60)
    video1 = models.CharField(max_length=40)
    video2 = models.CharField(max_length=40)
    video3 = models.CharField(max_length=40)
    video4 = models.CharField(max_length=40)
    chat = models.CharField(max_length=40, null=True, blank=True)

    def __str__(self):
        return self.title


class SixVideoStream(models.Model):

    title = models.CharField(max_length=60)
    video1 = models.CharField(max_length=40,)
    video2 = models.CharField(max_length=40)
    video3 = models.CharField(max_length=40)
    video4 = models.CharField(max_length=40)
    video5 = models.CharField(max_length=40)
    video6 = models.CharField(max_length=40)
    chat = models.CharField(max_length=40, null=True, blank=True)

    def __str__(self):
        return self.title