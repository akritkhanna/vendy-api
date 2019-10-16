from django.db import models

class Location(models.Model):

    latitude = models.DecimalField(verbose_name='latitude', decimal_places=7, max_digits=20)
    longitude = models.DecimalField(verbose_name='longitude', decimal_places=7, max_digits=20)
