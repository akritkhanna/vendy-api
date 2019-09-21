from django.db import models

class Location(models.Model):

    is_sharing = models.BooleanField(default=False)
    latitude = models.DecimalField(verbose_name='latitude', decimal_places=7, max_digits=10)
    longitude = models.DecimalField(verbose_name='longitude', decimal_places=7, max_digits=10)
