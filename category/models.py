from django.db import models


class Categories(models.Model):

    name = models.CharField(max_length=20)
    sub_types = models.ManyToManyField('category.SubCategories', default=None, blank=True, null=True)

    def __str__(self):
        return self.name


class SubCategories(models.Model):

    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


