from django.db import models


class Country(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)


    def __str__(self):
        return self.name