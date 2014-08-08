from django.db import models
from django.contrib import admin


class Region(models.Model):
    name = models.CharField(max_length=25)
    tva_percentage = models.FloatField()

    def __unicode__(self):
        return self.name


admin.site.register(Region)