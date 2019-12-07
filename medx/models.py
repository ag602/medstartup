from django.conf import settings
from django.db import models
from django.utils import timezone


class contact(models.Model):
    fname = models.CharField(max_length=100, null=True, blank=True,default=None)
    lname = models.CharField(max_length=100, null=True, blank=True,default=None)
    email = models.EmailField(blank=True)
    message = models.CharField(max_length=2000, null=True, blank=True,default=None)