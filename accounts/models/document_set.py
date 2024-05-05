from django.db import models
from accounts.models.country import Country

class DocumentSet(models.Model):
    document_name = models.CharField(max_length=255, null=True, blank=True)
    country_name = models.ManyToManyField(Country, related_name='country', blank=True)
    has_backside = models.BooleanField(default=False)
    ocr_labels  = models.TextField(blank=True, null= True)


    def __str__(self):
        return self.document_name