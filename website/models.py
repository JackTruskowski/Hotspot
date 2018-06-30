# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

#A sample model for testing Hotspot
class Sample(models.Model):
    restaurant_name = models.CharField(max_length=200)
    rating = models.FloatField()

#TODO: Production models
